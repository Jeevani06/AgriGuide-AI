import os
BASE = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-me")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE, "instance", "agriguide.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MODEL_DIR = os.path.join(BASE, "models")
    KB_DIR = os.path.join(BASE, "knowledge_base")
