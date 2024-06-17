from flask import jsonify, request, Blueprint
from database.database import db
from database.models import Notes
from common.read import get_all_data, get_data_by_id
from common.delete import delete_data_by_id
from common.create import create_data
from common.update import update_data
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)

notes_routes = Blueprint('note_routes', __name__)

@notes_routes.route('/notes', methods=["GET"])
def get_notes():
    logging.debug("GET /notes - Retrieving all notes")
    result = get_all_data(Notes)
    logging.debug(f"GET /notes - Retrieved {len(result)} notes")
    return jsonify(result)

@notes_routes.route('/notes', methods=['POST'])
def create_note():
    text = request.json.get("text", None)
    logging.debug(f"POST /notes - Creating note with text: {text}")
    result = create_data(Notes, db, text=text)
    logging.debug("POST /notes - Note created successfully")
    return result

@notes_routes.route("/notes/<int:id>", methods=["GET"])
def get_note(id):
    logging.debug(f"GET /notes/{id} - Retrieving note by ID")
    result = get_data_by_id(Notes, id)
    logging.debug(f"GET /notes/{id} - Note retrieved successfully")
    return jsonify(result)

@notes_routes.route('/notes/<int:id>', methods=['PUT'])
def update_note(id):
    new_text = request.json.get("text", None)
    logging.debug(f"PUT /notes/{id} - Updating note with new text: {new_text}")
    result = update_data(Notes, db, id, text=new_text)
    logging.debug(f"PUT /notes/{id} - Note updated successfully")
    return jsonify(result)

@notes_routes.route('/notes/<int:id>', methods=['DELETE'])
def delete_note(id):
    logging.debug(f"DELETE /notes/{id} - Deleting note by ID")
    result = delete_data_by_id(Notes, db, id)
    logging.debug(f"DELETE /notes/{id} - Note deleted successfully")
    return jsonify(result)