FEATS = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
def parse_floats(form, keys):
    """Return {key: float}; raises ValueError on missing/invalid input."""
    return {k: float(form[k]) for k in keys}
