import os, joblib
from flask import current_app
from ..utils.preprocessing import FEATS
_cache = {}
def _load():
    if not _cache:
        d = current_app.config["MODEL_DIR"]
        _cache["m"] = joblib.load(os.path.join(d, "crop_recommendation_model.pkl"))
        _cache["s"] = joblib.load(os.path.join(d, "scaler.pkl"))
    return _cache["m"], _cache["s"]
def top_crops(values, k=3):
    m, s = _load()
    p = m.predict_proba(s.transform([[values[f] for f in FEATS]]))[0]
    idx = p.argsort()[::-1][:k]
    return [(m.classes_[i], round(float(p[i]) * 100, 1)) for i in idx]
