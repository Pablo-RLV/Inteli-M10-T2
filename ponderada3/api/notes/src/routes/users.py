from database.database import db
from database.models import User
from flask import jsonify, request, Blueprint
from common.read import get_all_data, get_data_by_id
from common.delete import delete_data_by_id
from common.create import create_data
from common.update import update_data

users_routes = Blueprint('users_routes', __name__)

@users_routes.route("/users", methods=["GET"])
def get_users():
    result = get_all_data(User)
    return jsonify(result)

@users_routes.route("/users", methods=["POST"])
def create_user():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    result = create_data(User, db, username=username, password=password)
    return result

@users_routes.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    result = get_data_by_id(User, id)
    return jsonify(result)

@users_routes.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    new_username = request.json.get("username", None)
    new_password = request.json.get("password", None)
    result = update_data(User, db, id, username=new_username, password=new_password)
    return jsonify(result)

@users_routes.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    result = delete_data_by_id(User, db, id)
    return jsonify(result)