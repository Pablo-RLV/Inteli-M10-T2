import sys
import requests as http_request
from database.database import db
from flask import Flask, make_response, jsonify, request
from database.models import User, Notes
from flask_jwt_extended import JWTManager, set_access_cookies, create_access_token, jwt_required

app = Flask(__name__, template_folder="templates")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)
app.config["JWT_SECRET_KEY"] = "goku-vs-vegeta" 
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
jwt = JWTManager(app)

if len(sys.argv) > 1 and sys.argv[1] == 'create_db':
    with app.app_context():
        db.create_all()
    print("Database created successfully")
    sys.exit(0)

@app.route("/token", methods=["POST"])
def create_token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(username=username, password=password).first()
    if user is None:
        return jsonify({"msg": "Bad username or password"}), 401
    access_token = create_access_token(identity=user.id)
    return jsonify({ "token": access_token, "user_id": user.id })

@app.route("/")
def user_login():
    return "Hello, World!"

@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return_users = []
    for user in users:
        return_users.append(user.serialize())
    return jsonify(return_users)

@app.route("/users", methods=["POST"])
def create_user():
    username = request.form.get("username", None)
    password = request.form.get("password", None)
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize())

@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get(id)
    return jsonify(user.serialize())

@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    username = request.form.get("username", None)
    password = request.form.get("password", None)
    user = User.query.get(id)
    user.username = username
    user.password = password
    db.session.commit()
    return jsonify(user.serialize())

@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(user.serialize())

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", None)
    password = request.form.get("password", None)
    if username is None or password is None:
        return "Bad username or password"
    token_data = http_request.post("http://localhost:5000/token", json={"username": username, "password": password})
    if token_data.status_code != 200:
        return "Bad username or password"
    response = make_response("Login successful")
    set_access_cookies(response, token_data.json()['token'])
    return response

@app.route('/notes', methods=["GET"])
@jwt_required()
def get_notes():
    notes = Notes.query.all()
    return_notes = []
    for note in notes:
        return_notes.append(note.serialize())
    return jsonify(return_notes)

@app.route('/notes' , methods = ['POST'])
@jwt_required()
def create_note():
    text = request.form.get("text", None)
    note = Notes(text=text)
    db.session.add(note)
    db.session.commit()
    return jsonify(note.serialize())

@app.route("/notes/<int:id>", methods=["GET"])
def get_note(id):
    note = Notes.query.get(id)
    return jsonify(note.serialize())
    
@app.route('/notes/<int:id>',methods = ['PUT'])
@jwt_required()
def update_note(id):
    new_text = request.form.get("text", None)
    note = Notes.query.get(id)
    note.text = new_text
    db.session.commit()
    return jsonify(note.serialize())

@app.route('/notes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_note(id):
    note = Notes.query.get(id)
    db.session.delete(note)
    db.session.commit()
    return jsonify(note.serialize())