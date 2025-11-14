from flask import Blueprint, request
from models.users import User
from models.db import db

users = Blueprint('users', __name__, url_prefix='/users')

@users.route('/', methods=['GET'])
def get_users():
    return "List of users"


@users.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if User.query.filter_by(email=email).first():
        return {'message': 'Email already registered'}, 400

    new_user = User(username=username, password=password, email=email)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return {'message': 'User registered successfully'}, 201