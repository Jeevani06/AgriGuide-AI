import json, os
from flask import current_app

def analyze(crop, obs):
    """Compare observations with the crop's ideal ranges -> (level, alerts)."""
    kb = json.load(open(os.path.join(current_app.config["KB_DIR"], "crops.json")))
    ideal, alerts, score = kb[crop], [], 0
    for k, v in obs.items():
        if k not in ideal: continue
        lo, hi = ideal[k]; span = hi - lo or 1
        if v < lo or v > hi:
            dev = (lo - v if v < lo else v - hi) / span
            score += 2 if dev > .5 else 1
            alerts.append(f"{k} is {'low' if v < lo else 'high'} ({v:g}; ideal {lo:g}-{hi:g})")
    level = "LOW" if score == 0 else "MEDIUM" if score <= 3 else "HIGH"
    return level, alerts
