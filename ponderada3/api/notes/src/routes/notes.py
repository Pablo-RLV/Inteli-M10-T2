from database.database import db
from database.models import Notes
from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required
from common.read import get_all_data, get_data_by_id
from common.delete import delete_data_by_id
from common.create import create_data
from common.update import update_data

notes_routes = Blueprint('note_routes', __name__)

@notes_routes.route('/notes', methods=["GET"])
@jwt_required()
def get_notes():
    result = get_all_data(Notes)
    return jsonify(result)

@notes_routes.route('/notes' , methods = ['POST'])
@jwt_required()
def create_note():
    text = request.json.get("text", None)
    result = create_data(Notes, db, text=text)
    return result

@notes_routes.route("/notes/<int:id>", methods=["GET"])
@jwt_required()
def get_note(id):
    result = get_data_by_id(Notes, id)
    return jsonify(result)
    
@notes_routes.route('/notes/<int:id>',methods = ['PUT'])
@jwt_required()
def update_note(id):
    new_text = request.json.get("text", None)
    result = update_data(Notes, db, id, text=new_text)
    return jsonify(result)

@notes_routes.route('/notes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_note(id):
    result = delete_data_by_id(Notes, db, id)
    return jsonify(result)