from flask import Blueprint, jsonify, request
from coordenador_api import *

disciplinaofertada_app = Blueprint('disciplinaofertada_app', __name__, template_folder='templates')
disciplinaofertada_db = []

@disciplinaofertada_app.route('/disciplinaofertada', methods=['GET'])
def listar():
    return jsonify(disciplinaofertada_db)

@disciplinaofertada_app.route('/disciplinsofertada/<int:id_disciplinaofertada>', methods=['GET'])
def localiza(id_disciplinaofertada):
    for disciplinaofertada in disciplinaofertada_db:
        if disciplinaofertada['id'] == id_disciplinaofertada:
            return jsonify(disciplinaofertada)
    return '', 404

@disciplinaofertada_app.route('/disciplinaofertada', methods=['POST'])
def novo():
    novo_disciplinaofertada = request.get_json()
    disciplinaofertada_db.append(novo_disciplinaofertada)
    disciplina = request.get_json()
    disciplinaofertada_db.append(disciplina)
    professor = request.get_json()
    disciplinaofertada_db.append(professor)
    turma = request.get_json()
    disciplinaofertada_db.append(turma)
    ano = request.get_json()
    disciplinaofertada_db.append(ano)
    semestre = request.get_json()
    disciplinaofertada_db.append(semestre)
    return jsonify(disciplinaofertada_db)

@disciplinaofertada_app.route('/disciplinaofertada/<int:id_disciplinaofertada>', methods=['DELETE'])
def remover(id_disciplina):
    index = 0
    for disciplinaofertada in disciplinaofertada_db:
        if disciplinaofertada['id'] == id_disciplinaofertada:
            del disciplinaofertada_db[index]
            return jsonify(disciplinaofertada)
        index = index + 1
    return '', 404

@disciplinaofertada_app.route('/disciplinaofertada/<int:id_disciplinaofertada>', methods=['PUT'])
def atualiza(id_disciplinaofertada):
    novo_disciplinaofertada = request.get_json()
    index = 0
    for disciplinaofertada in disciplinaofertada_db:
        if disciplinaofertada['id'] == id_disciplinaofertada:
            del disciplinaofertada_db[index]
            disciplinaofertada_db.append(novo_disciplinaofertada)
            return jsonify(disciplinaofertada)
        index = index + 1
    return '', 404