from app.models.user import User 

from app import db
from sqlalchemy.exc import IntegrityError

def get_all_users():
    return User.query.all()

def get_user_by_id(user_id: int):
    return User.query.get_or_404(user_id)

def create_user(data: dict):
    user = User(name=data['name'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise
    return user

def update_user(user_id: int, data: dict):
    user = get_user_by_id(user_id)
    if 'name' in data:
        user.name = data['name']
    if 'email' in data:
        user.email = data['email']
    if 'password' in data:
        user.set_password(data['password'])
    db.session.commit()
    return user

def delete_user(user_id: int):
    user = get_user_by_id(user_id)
    db.session.delete(user)
    db.session.commit()
    return user

def search_users_by_name(name_substr: str):
    return User.query.filter(User.name.ilike(f'%{name_substr}%')).all()
