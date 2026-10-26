import json
from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from ..database.db import db
from ..database.models import Record
from ..utils.risk_analysis import analyze
from ..utils.preprocessing import parse_floats
bp = Blueprint("monitor", __name__)
FIELDS = ["soil_moisture", "N", "P", "K", "temperature", "humidity", "rainfall"]

@bp.route("/monitor", methods=["GET", "POST"])
@login_required
def monitor():
    out, kb_crops = None, None
    from .recommendation import kb
    kb_crops = list(kb("crops.json"))
    if request.method == "POST":
        try:
            obs = parse_floats(request.form, FIELDS); crop = request.form["crop"]
            level, alerts = analyze(crop, obs)
            obs["growth_stage"] = request.form.get("growth_stage", "")
            out = {"level": level, "alerts": alerts, "crop": crop}
            db.session.add(Record(user_id=current_user.id, kind="monitoring", crop=crop,
                summary=f"Risk {level}: {len(alerts)} alert(s)", data=json.dumps({**obs, "alerts": alerts})))
            db.session.commit()
        except (ValueError, KeyError):
            flash("Please enter valid numbers in every field.", "danger")
    return render_template("monitor.html", out=out, fields=FIELDS, crops=kb_crops)
