from flask import Blueprint, request, jsonify
from controllers.userController import get_all_users

user_bd = Blueprint('users', __name__)
@user_bd.route('/', methods=['GET'])
def index():
    user = get_all_users()
    return jsonify({})