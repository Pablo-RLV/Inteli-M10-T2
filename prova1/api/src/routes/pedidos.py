from database.database import db
from database.models import Pedidos
from flask import jsonify, request, Blueprint
from common.read import get_all_data, get_data_by_id
from common.delete import delete_data_by_id
from common.create import create_data
from common.update import update_data

pedidos_routes = Blueprint('pedidos_routes', __name__)

@pedidos_routes.route("/pedidos", methods=["GET"])
def get_users():
    result = get_all_data(Pedidos)
    return jsonify(result)

@pedidos_routes.route("/pedidos", methods=["POST"])
def create_user():
    nome = request.json.get("nome", None)
    email = request.json.get("email", None)
    descricao = request.json.get("descricao", None)
    result = create_data(Pedidos, db, nome=nome, email=email, descricao=descricao)
    return result

@pedidos_routes.route("/pedidos/<int:id>", methods=["GET"])
def get_user(id):
    result = get_data_by_id(Pedidos, id)
    return jsonify(result)

@pedidos_routes.route("/pedidos/<int:id>", methods=["PUT"])
def update_user(id):
    new_nome = request.json.get("nome", None)
    new_email = request.json.get("email", None)
    new_descricao = request.json.get("descricao", None)
    result = update_data(Pedidos, db, id, nome=new_nome, email=new_email, descricao=new_descricao)
    return jsonify(result)

@pedidos_routes.route("/pedidos/<int:id>", methods=["DELETE"])
def delete_user(id):
    result = delete_data_by_id(Pedidos, db, id)
    return jsonify(result)

@pedidos_routes.route("/novo", methods=["POST"])
def new_user():
    nome = request.json.get("nome", None)
    email = request.json.get("email", None)
    descricao = request.json.get("descricao", None)
    db.session.add(Pedidos(nome=nome, email=email, descricao=descricao))
    db.session.commit()
    return jsonify({"id": Pedidos.query.filter_by(nome=nome).first().id})