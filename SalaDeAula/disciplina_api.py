from flask import Blueprint, jsonify, request
from coordenador_api import *

disciplina_app = Blueprint('disciplina_app', __name__, template_folder='templates')
disciplina_db = []

@disciplina_app.route('/disciplina', methods=['GET'])
def listar():
    return jsonify(disciplina_db)

@disciplina_app.route('/disciplinas/<int:id_disciplina>', methods=['GET'])
def localiza(id_disciplina):
    for disciplina in disciplinas_db:
        if disciplina['id'] == id_disciplina:
            return jsonify(disciplina)
    return '', 404

@disciplina_app.route('/disciplinas', methods=['POST'])
def novo():
    novo_disciplina = request.get_json()
    disciplinas_db.append(novo_disciplina)
    return jsonify(disciplinas_db)

@disciplina_app.route('/disciplinas/<int:id_disciplina>', methods=['DELETE'])
def remover(id_disciplina):
    index = 0
    for disciplina in disciplinas_db:
        if disciplina['id'] == id_disciplina:
            del disciplinas_db[index]
            return jsonify(disciplina)
        index = index + 1
    return '', 404

@disciplina_app.route('/disciplinas/<int:id_disciplina>', methods=['PUT'])
def atualiza(id_disciplina):
    novo_disciplina = request.get_json()
    index = 0
    for disciplina in disciplinas_db:
        if disciplina['id'] == id_disciplina:
            del disciplinas_db[index]
            disciplinas_db.append(novo_disciplina)
            return jsonify(disciplina)
        index = index + 1
    return '', 404