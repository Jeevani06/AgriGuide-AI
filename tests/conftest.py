import os, sys, pytest
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from config import Config
from app import create_app
class T(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
@pytest.fixture
def client():
    return create_app(T).test_client()
