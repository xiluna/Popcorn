from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    """Set environment variables."""

    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    FLASK_ENV = 'development'
