import json
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .db import db, login_manager

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    def set_password(self, p): self.password_hash = generate_password_hash(p)
    def check_password(self, p): return check_password_hash(self.password_hash, p)

class Record(db.Model):
    """One row per action: kind = recommendation | monitoring | yield."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    kind = db.Column(db.String(20), nullable=False)
    crop = db.Column(db.String(50))
    summary = db.Column(db.String(200))
    data = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    def payload(self): return json.loads(self.data or "{}")

@login_manager.user_loader
def load_user(uid): return db.session.get(User, int(uid))
