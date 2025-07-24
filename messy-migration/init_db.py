from app import create_app
from app.extensions import db  # ✅

def seed_data():
    from app.models.user import User  # ✅
    ...

    users = [
        User(name='Alice', email='alice@example.com'),
        User(name='Bob', email='bob@example.com'),
    ]
    for u in users:
        u.set_password('password123')
        db.session.add(u)
    db.session.commit()
    print('Seed data inserted.')

def main():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        seed_data()

if __name__ == '__main__':
    main()


