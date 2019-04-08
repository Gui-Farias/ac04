from flask import Blueprint, jsonify, request

coordenador_app = Blueprint('coordenador_app', __name__, template_folder='templates')
coordenador_db = []

@coordenador_app.route('/coordenador', methods=['GET'])
def listar():
    return jsonify(coordenador_db)

@coordenador_app.route('/coordenador/<int:id_coordenador>', methods=['GET'])
def localiza(id_coordenador):
    for coordenador in coordenador_db:
        if coordenador['id'] == id_coordenador:
            return jsonify(coordenador)
    return '', 404

@coordenador_app.route('/coordenador', methods=['POST'])
def novo():
    novo_coodenador = request.get_json()
    coordenador_db.append(novo_coodenador)
    return jsonify(coordenador_db)

@coordenador_app.route('/coordenador/<int:id_coordenador>', methods=['DELETE'])
def remover(id_coordenador):
    index = 0
    for coordenador in coordenador_db:
        if coordenador['id'] == id_coordenador:
            del coordenador_db[index]
            return jsonify(coordenador)
        index = index + 1
    return '', 404

@coordenador_app.route('/coordenador/<int:id_coordenador>', methods=['PUT'])
def atualiza(id_coordenador):
    novo_coodenador = request.get_json()
    index = 0
    for coordenador in coordenador_db:
        if coordenador['id'] == id_coordenador:
            del coordenador_db[index]
            coordenador_db.append(novo_coodenador)
            return jsonify(coordenador)
        index = index + 1
    return '', 404