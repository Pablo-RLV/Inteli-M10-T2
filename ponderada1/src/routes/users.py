from database.database import db
from database.models import User
from flask import jsonify, request, Blueprint

users_routes = Blueprint('users_routes', __name__)

@users_routes.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return_users = []
    for user in users:
        return_users.append(user.serialize())
    return jsonify(return_users)

@users_routes.route("/users", methods=["POST"])
def create_user():
    username = request.form.get("username", None)
    password = request.form.get("password", None)
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize())

@users_routes.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get(id)
    return jsonify(user.serialize())

@users_routes.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    username = request.form.get("username", None)
    password = request.form.get("password", None)
    user = User.query.get(id)
    user.username = username
    user.password = password
    db.session.commit()
    return jsonify(user.serialize())

@users_routes.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(user.serialize())