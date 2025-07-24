import jwt
from datetime import datetime, timedelta
from flask import current_app
from app.models.user import User
from app.extensions import db

def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return user
    return None

def generate_token(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(payload, current_app.config['JWT_SECRET_KEY'], algorithm='HS256')
    return token
