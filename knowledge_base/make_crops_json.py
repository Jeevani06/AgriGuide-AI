import json, pandas as pd
df = pd.read_csv("data/raw/crop_recommendation.csv")
old = json.load(open("knowledge_base/crops.json"))
feats = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
out = {}
for crop, g in df.groupby("label"):
    out[crop] = {f: [round(g[f].quantile(.1), 1), round(g[f].quantile(.9), 1)] for f in feats}
    out[crop]["soil_moisture"] = old.get(crop, {}).get("soil_moisture", [30, 70])
json.dump(out, open("knowledge_base/crops.json", "w"), indent=1)
print(len(out), "crops written")