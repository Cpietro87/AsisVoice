from flask import Blueprint
from models.users import User

routes_auth = Blueprint('routes_auth', __name__,)

@routes_auth.route('/login', methods=['GET', 'POST'] )
def login():
    return "Login Page"