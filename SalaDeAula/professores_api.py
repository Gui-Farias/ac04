from flask import Blueprint, jsonify, request
professores_app = Blueprint('professores_app', __name__, template_folder='templates')
professores_db = []

@professores_app.route('/professores', methods=['GET'])
def listar():
    return jsonify(professores_db)

@professores_app.route('/professores/<int:matricula>', methods=['GET'])
def localiza(matricula):
    for p in professores_db:
        if p['matricula'] == matricula:
            return jsonify(p)
    return '', 404

@professores_app.route('/professores', methods=['POST'])
def novo():
    novo_professor = request.get_json()
    professores_db.append(novo_professor)
    return jsonify(professores_db)

@professores_app.route('/professores/<int:matricula>', methods=['DELETE'])
def remover(matricula):
    index = 0
    for p in professores_db:
        if p['id'] == matricula:
            del professores_db[index]
            return jsonify(p)
        index = index + 1
    return '', 404

@professores_app.route('/professores/<int:matricula>', methods=['PUT'])
def atualiza(matricula):
    novo_professor = request.get_json()
    index = 0
    for p in professores_db:
        if p['matricula'] == matricula:
            del professores_db[index]
            professores_db.append(novo_professor)
            return jsonify(p)
        index = index + 1
    return '', 404