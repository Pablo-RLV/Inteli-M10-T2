import requests as http_request
from database.models import User
from flask import jsonify, request, Blueprint, make_response
from flask_jwt_extended import set_access_cookies, create_access_token

auth_routes = Blueprint('auth_routes', __name__)


@auth_routes.route("/token", methods=["POST"])
async def create_token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(username=username, password=password).first()
    if user is None:
        return jsonify({"msg": "Bad username or password"}), 401
    access_token = create_access_token(identity=user.id)
    return jsonify({ "token": access_token, "user_id": user.id })

@auth_routes.route("/login", methods=["POST"])
async def login():
    username = request.form.get("username", None)
    password = request.form.get("password", None)
    if username is None or password is None:
        return "Bad username or password"
    token_data = http_request.post("http://localhost:5001/token", json={"username": username, "password": password})
    if token_data.status_code != 200:
        return "Bad username or password"
    response = make_response("Login successful")
    set_access_cookies(response, token_data.json()['token'])
    return response