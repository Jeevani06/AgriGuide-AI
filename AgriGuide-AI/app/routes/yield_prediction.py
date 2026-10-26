import json
from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from ..database.db import db
from ..database.models import Record
from ..ml import yield_predictor as yp
bp = Blueprint("yield_pred", __name__)

@bp.route("/yield", methods=["GET", "POST"])
@login_required
def predict():
    res = None
    if request.method == "POST":
        try:
            crop = request.form["crop"]; f = request.form
            rain, fert, pest = float(f["rainfall"]), float(f["fertilizer"]), float(f["pesticide"])
            res = {"crop": crop, "value": yp.predict(crop, rain, fert, pest)}
            db.session.add(Record(user_id=current_user.id, kind="yield", crop=crop,
                summary=f"Expected yield {res['value']} tons/ha",
                data=json.dumps({"rainfall": rain, "fertilizer": fert, "pesticide": pest, "yield": res["value"]})))
            db.session.commit()
        except (ValueError, KeyError):
            flash("Please enter valid numbers.", "danger")
    return render_template("yield_prediction.html", res=res, crops=yp.crops())
