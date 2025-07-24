import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'super-jwt-secret')
    SECRET_KEY = os.getenv('SECRET_KEY', 'change-me')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///users.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


