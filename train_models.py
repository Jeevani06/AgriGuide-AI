"""Train models. Uses data/raw CSVs if present, else synthetic data so the app runs end-to-end."""
import os, json, joblib, numpy as np, pandas as pd
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from config import Config
FEATS = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
kb = json.load(open(os.path.join(Config.KB_DIR, "crops.json")))
rng = np.random.default_rng(0)
raw = "data/raw/crop_recommendation.csv"
if os.path.exists(raw):
    df = pd.read_csv(raw).dropna()
else:
    rows = []
    for c, p in kb.items():
        for _ in range(200):
            r = {f: rng.uniform(*p[f]) + rng.normal(0, 3 if f != "ph" else .2) for f in FEATS}
            r["label"] = c; rows.append(r)
    df = pd.DataFrame(rows)
df.to_csv("data/processed/crop_recommendation_clean.csv", index=False)
sc = StandardScaler().fit(df[FEATS])
Xtr, Xte, ytr, yte = train_test_split(sc.transform(df[FEATS]), df["label"], test_size=.2, random_state=1)
clf = RandomForestClassifier(200, random_state=1).fit(Xtr, ytr)
print("crop accuracy:", clf.score(Xte, yte))
joblib.dump(clf, "models/crop_recommendation_model.pkl"); joblib.dump(sc, "models/scaler.pkl")

# Yield: Crop, Annual_Rainfall, Fertilizer, Pesticide -> Yield (t/ha)
raw = "data/raw/crop_yield.csv"
if os.path.exists(raw):
    y = pd.read_csv(raw).dropna()[["Crop", "Annual_Rainfall", "Fertilizer", "Pesticide", "Yield"]]
    y["Crop"] = y["Crop"].str.strip().str.lower()
else:
    n = 1500; crops = list(kb)
    y = pd.DataFrame({"Crop": rng.choice(crops, n), "Annual_Rainfall": rng.uniform(300, 2500, n),
                      "Fertilizer": rng.uniform(50, 300, n), "Pesticide": rng.uniform(0.2, 5, n)})
    y["Yield"] = 1.5 + y.Annual_Rainfall / 900 + y.Fertilizer / 120 + y.Pesticide * .2 + rng.normal(0, .3, n)
y.to_csv("data/processed/crop_yield_clean.csv", index=False)
crops = sorted(y["Crop"].unique())
X = pd.DataFrame({"crop": y["Crop"].map({c: i for i, c in enumerate(crops)}), "rain": y.Annual_Rainfall,
                  "fert": y.Fertilizer, "pest": y.Pesticide})
reg = RandomForestRegressor(200, random_state=1).fit(X, y["Yield"])
joblib.dump({"model": reg, "crops": crops}, "models/yield_prediction_model.pkl")
print("yield R2 (train):", reg.score(X, y["Yield"]))
