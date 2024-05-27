from database.database import db
from database.models import Notes
from flask import jsonify, request, Blueprint
from common.read import get_all_data, get_data_by_id
from common.delete import delete_data_by_id
from common.create import create_data
from common.update import update_data

notes_routes = Blueprint('note_routes', __name__)

@notes_routes.route('/notes', methods=["GET"])
def get_notes():
    result = get_all_data(Notes)
    return jsonify(result)

@notes_routes.route('/notes' , methods = ['POST'])
def create_note():
    text = request.json.get("text", None)
    result = create_data(Notes, db, text=text)
    return result

@notes_routes.route("/notes/<int:id>", methods=["GET"])
def get_note(id):
    result = get_data_by_id(Notes, id)
    return jsonify(result)
    
@notes_routes.route('/notes/<int:id>',methods = ['PUT'])
def update_note(id):
    new_text = request.json.get("text", None)
    result = update_data(Notes, db, id, text=new_text)
    return jsonify(result)

@notes_routes.route('/notes/<int:id>', methods=['DELETE'])
def delete_note(id):
    result = delete_data_by_id(Notes, db, id)
    return jsonify(result)