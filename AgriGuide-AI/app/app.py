import os
from flask import Flask, Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from config import Config
from .database.db import db, login_manager
from .database.models import Record
main = Blueprint("main", __name__)

@main.route("/")
def index():
    return redirect(url_for("main.dashboard"))

@main.route("/dashboard")
@login_required
def dashboard():
    recs = Record.query.filter_by(user_id=current_user.id).order_by(Record.created.desc())
    latest = {k: recs.filter_by(kind=k).first() for k in ("recommendation", "monitoring", "yield")}
    risks = [r.summary.split(":")[0].replace("Risk ", "") for r in recs.filter_by(kind="monitoring").limit(10)][::-1]
    return render_template("dashboard.html", latest=latest, risks=risks)

@main.route("/history")
@login_required
def history():
    recs = Record.query.filter_by(user_id=current_user.id).order_by(Record.created.desc()).all()
    return render_template("history.html", recs=recs)

def create_app(config=Config):
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config.from_object(config)
    os.makedirs(os.path.join(Config.BASE if hasattr(Config, "BASE") else ".", "instance"), exist_ok=True)
    db.init_app(app); login_manager.init_app(app)
    from .routes import auth, recommendation, monitoring, yield_prediction
    for m in (auth, recommendation, monitoring, yield_prediction):
        app.register_blueprint(m.bp)
    app.register_blueprint(main)
    with app.app_context():
        db.create_all()
    return app
