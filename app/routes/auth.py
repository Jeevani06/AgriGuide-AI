from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from ..database.db import db
from ..database.models import User
bp = Blueprint("auth", __name__)

@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        f = request.form
        if User.query.filter_by(email=f["email"]).first():
            flash("Email already registered.", "danger")
        else:
            u = User(name=f["name"], email=f["email"]); u.set_password(f["password"])
            db.session.add(u); db.session.commit()
            return redirect(url_for("auth.login"))
    return render_template("register.html")

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = User.query.filter_by(email=request.form["email"]).first()
        if u and u.check_password(request.form["password"]):
            login_user(u); return redirect(url_for("main.dashboard"))
        flash("Invalid credentials.", "danger")
    return render_template("login.html")

@bp.route("/logout")
def logout():
    logout_user(); return redirect(url_for("auth.login"))
