from flask import Blueprint, jsonify, request
curso_app = Blueprint('curso_app', __name__, template_folder='templates')
curso_db = []

@curso_app.route('/curso', methods=['GET'])
def listar():
    return jsonify(curso_db)

@curso_app.route('/curso/<int:id_curso>', methods=['GET'])
def localiza(id_curso):
    for curso in curso_db:
        if curso['id'] == id_curso:
            return jsonify(curso)
    return '', 404

@curso_app.route('/curso', methods=['POST'])
def novo():
    novo_curso = request.get_json()
    curso_db.append(novo_curso)
    return jsonify(curso_db)

@curso_app.route('/curso/<int:id_curso>', methods=['DELETE'])
def remover(id_curso):
    index = 0
    for curso in curso_db:
        if curso['id'] == id_curso:
            del curso_db[index]
            return jsonify(curso)
        index = index + 1
    return '', 404

@curso_app.route('/curso/<int:id_curso>', methods=['PUT'])
def atualiza(id_aluno):
    novo_curso = request.get_json()
    index = 0
    for curso in curso_db:
        if curso['id'] == id_curso:
            del curso_db[index]
            curso_db.append(novo_curso)
            return jsonify(curso)
        index = index + 1
    return '', 404