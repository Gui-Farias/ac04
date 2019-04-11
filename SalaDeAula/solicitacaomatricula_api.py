from flask import Blueprint, jsonify, request
from coordenador_api import *

solicitacaomatricula_app = Blueprint('solicitacaomatricula_app', __name__, template_folder='templates')
solicitacaomatricula_db = []

@solicitacaomatricula_app.route('/solicitacaomatricula', methods=['GET'])
def listar():
    return jsonify(solicitacaomatricula_db)

@solicitacaomatricula_app.route('/disciplinsofertada/<int:id_solicitacaomatricula>', methods=['GET'])
def localiza(id_solicitacaomatricula):
    for solicitacaomatricula in solicitacaomatricula_db:
        if solicitacaomatricula['id'] == id_disciplinaofertada:
            return jsonify(solicitacaomatricula)
    return '', 404

@solicitacaomatricula_app.route('/solicitacaomatricula', methods=['POST'])
def novo():
    novo_solicitacaomatricula = request.get_json()
    solicitacaomatricula_db.append(novo_solicitacaomatricula)
    aluno = request.get_json()
    solicitacaomatricula_db.append(aluno)
    disciplinaofertada = request.get_json()
    solicitacaomatricula_db.append(disciplinaofertada)
    coordenador = request.get_json()
    solicitacaomatricula_db.append(coordenador)
    status = request.get_json()
    solicitacaomatricula_db.append(status)
    sdata = request.get_json()
    solicitacaomatricula_db.append(sdata)
    return jsonify(solicitacaomatricula_db)

@solicitacaomatricula_app.route('/solicitacaomatricula/<int:id_solicitacaomatricula>', methods=['DELETE'])
def remover(id_disciplina):
    index = 0
    for solicitacaomatricula in solicitacaomatricula_db:
        if solicitacaomatricula['id'] == id_solicitacaomatricula:
            del solicitacaomatricula_db[index]
            return jsonify(solicitacaomatricula)
        index = index + 1
    return '', 404

@solicitacaomatricula_app.route('/solicitacaomatricula/<int:id_solicitacaomatricula>', methods=['PUT'])
def atualiza(id_solicitacaomatricula):
    novo_solicitacaomatricula = request.get_json()
    index = 0
    for solicitacaomatricula in solicitacaomatricula_db:
        if solicitacaomatricula['id'] == id_solicitacaomatricula:
            del solicitacaomatricula_db[index]
            solicitacaomatricula_db.append(novo_solicitacaomatricula)
            return jsonify(solicitacaomatricula)
        index = index + 1
    return '', 404