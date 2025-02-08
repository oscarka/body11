import os

class Config:
    SECRET_KEY = os.environ.get("RAILWAY_SECRET_KEY", "dev")
    SQLALCHEMY_DATABASE_URI = os.environ.get("RAILWAY_DATABASE_URL", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
