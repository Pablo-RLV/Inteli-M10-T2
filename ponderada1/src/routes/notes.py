from database.database import db
from database.models import Notes
from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required

notes_routes = Blueprint('note_routes', __name__)

@notes_routes.route('/notes', methods=["GET"])
@jwt_required()
def get_notes():
    notes = Notes.query.all()
    return_notes = []
    for note in notes:
        return_notes.append(note.serialize())
    return jsonify(return_notes)

@notes_routes.route('/notes' , methods = ['POST'])
@jwt_required()
def create_note():
    text = request.form.get("text", None)
    note = Notes(text=text)
    db.session.add(note)
    db.session.commit()
    return jsonify(note.serialize())

@notes_routes.route("/notes/<int:id>", methods=["GET"])
def get_note(id):
    note = Notes.query.get(id)
    return jsonify(note.serialize())
    
@notes_routes.route('/notes/<int:id>',methods = ['PUT'])
@jwt_required()
def update_note(id):
    new_text = request.form.get("text", None)
    note = Notes.query.get(id)
    note.text = new_text
    db.session.commit()
    return jsonify(note.serialize())

@notes_routes.route('/notes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_note(id):
    note = Notes.query.get(id)
    db.session.delete(note)
    db.session.commit()
    return jsonify(note.serialize())