import pytest
import json
from app import create_app, db
from models.user import User

@pytest.fixture
def client():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        user = User(name='Test', email='test@example.com')
        user.set_password('pass123')
        db.session.add(user)
        db.session.commit()
    return app.test_client()


def test_health_check(client):
    res = client.get('/')
    data = res.get_json()
    assert res.status_code == 200
    assert data['status'] == 'success'


def test_list_users(client):
    res = client.get('/users')
    assert res.status_code == 200
    assert isinstance(res.get_json()['data'], list)


def test_create_user(client):
    payload = {'name': 'Jane', 'email': 'jane@example.com', 'password': 'secret'}
    res = client.post('/users', json=payload)
    assert res.status_code == 201
    assert res.get_json()['data']['email'] == 'jane@example.com'


def test_get_user(client):
    res = client.get('/users/1')
    assert res.status_code == 200
    assert res.get_json()['data']['email'] == 'test@example.com'


def test_update_user(client):
    res = client.put('/users/1', json={'name': 'Tester'})
    assert res.status_code == 200
    assert res.get_json()['data']['name'] == 'Tester'


def test_delete_user(client):
    res = client.delete('/users/1')
    assert res.status_code == 200
    res2 = client.get('/users/1')
    assert res2.status_code == 404
