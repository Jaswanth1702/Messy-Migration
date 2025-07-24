from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.schemas.user_schema import UserSchema  # ✅
from app.services.user_service import (         # ✅
    get_all_users, get_user_by_id, create_user,
    update_user, delete_user, search_users_by_name
)


user_bp = Blueprint('user_bp', __name__)
schema = UserSchema()
schema_many = UserSchema(many=True)

from app.services.auth_service import authenticate_user, generate_token

@user_bp.route('/login', methods=['POST'])
def login():
    json_data = request.get_json()
    email = json_data.get('email')
    password = json_data.get('password')

    if not email or not password:
        return jsonify({'status': 'error', 'message': 'Email and password required'}), 400

    user = authenticate_user(email, password)
    if not user:
        return jsonify({'status': 'error', 'message': 'Invalid credentials'}), 401

    token = generate_token(user)
    return jsonify({
        'status': 'success',
        'message': 'Login successful',
        'token': token,
        'expires_in': 3600
    }), 200


def format_response(data=None, message='', status='success'):
    return {'status': status, 'data': data, 'message': message}

@user_bp.route('/users', methods=['GET'])
def list_users():
    users = get_all_users()
    return jsonify(format_response(schema_many.dump(users))), 200

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    return jsonify(format_response(schema.dump(user))), 200

@user_bp.route('/users', methods=['POST'])
def add_user():
    json_data = request.get_json()
    try:
        data = schema.load(json_data)
    except ValidationError as err:
        return jsonify(format_response(err.messages, 'Validation failed', 'error')), 400

    try:
        user = create_user(data)
    except Exception:
        return jsonify(format_response(None, 'Email already exists', 'error')), 409

    return jsonify(format_response(schema.dump(user), 'User created')), 201

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    json_data = request.get_json()
    try:
        data = schema.load(json_data, partial=True)
    except ValidationError as err:
        return jsonify(format_response(err.messages, 'Validation failed', 'error')), 400

    user = update_user(user_id, data)
    return jsonify(format_response(schema.dump(user), 'User updated')), 200

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    delete_user(user_id)
    return jsonify(format_response(None, 'User deleted')), 200

@user_bp.route('/search')
def search_users():
    name = request.args.get('name', '')
    users = search_users_by_name(name)
    return jsonify(format_response(schema_many.dump(users))), 200
