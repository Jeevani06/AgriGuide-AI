import os, joblib, pandas as pd
from flask import current_app
_cache = {}
def crops():
    return _load()["crops"]
def _load():
    if not _cache:
        _cache.update(joblib.load(os.path.join(current_app.config["MODEL_DIR"], "yield_prediction_model.pkl")))
    return _cache
def predict(crop, rain, fert, pest):
    d = _load()
    X = pd.DataFrame([{"crop": d["crops"].index(crop), "rain": rain, "fert": fert, "pest": pest}])
    return round(float(d["model"].predict(X)[0]), 2)
