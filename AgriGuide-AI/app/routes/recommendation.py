import json, os
from flask import Blueprint, render_template, request, current_app, flash, abort
from flask_login import login_required, current_user
from ..database.db import db
from ..database.models import Record
from ..ml.crop_predictor import top_crops
from ..utils.preprocessing import FEATS, parse_floats
bp = Blueprint("recommend", __name__)

def kb(name):
    return json.load(open(os.path.join(current_app.config["KB_DIR"], name)))

@bp.route("/recommend", methods=["GET", "POST"])
@login_required
def recommend():
    results = None
    if request.method == "POST":
        try:
            vals = parse_floats(request.form, FEATS)
            results = top_crops(vals)
            db.session.add(Record(user_id=current_user.id, kind="recommendation", crop=results[0][0],
                summary=", ".join(f"{c} {p}%" for c, p in results), data=json.dumps(vals)))
            db.session.commit()
        except (ValueError, KeyError):
            flash("Please enter valid numbers in every field.", "danger")
    return render_template("recommend.html", results=results, feats=FEATS)

@bp.route("/crop/<crop>")
@login_required
def crop_guide(crop):
    crops = kb("crops.json")
    if crop not in crops: abort(404)
    g = kb("management_guidelines.json"); guide = {**g["default"], **g.get(crop, {})}
    st = kb("growth_stages.json"); stages = st.get(crop, st["default"])
    return render_template("crop_guide.html", crop=crop, guide=guide, stages=stages, ideal=crops[crop])
