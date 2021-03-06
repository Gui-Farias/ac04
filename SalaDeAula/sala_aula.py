from flask import Flask, jsonify, request
from alunos_api import alunos_app, alunos_db
from professores_api import professores_app, professores_db
from coordenador_api import coordenador_app, coordenador_db
from curso_api import curso_app, curso_db
from disciplina_api import disciplina_app, disciplina_db
from disciplinaofertada_api import disciplinaofertada_app, disciplinaofertada_db
from solicitacaomatricula_api import solicitacaomatricula_app, solicitacaomatricula_db

database = {
    "ALUNOS" : alunos_db,
    "PROFESSORES" : professores_db,
    "COORDENADOR" : coordenador_db,
    "CURSO" : curso_db,
    "DISCIPLINA" : disciplina_db,
    "DISCIPLINAOFERTADA" : disciplinaofertada_db,
    "SOLICITACAOMATRICULA" : solicitacaomatricula_db,
}

app = Flask(__name__)
app.register_blueprint(alunos_app)
app.register_blueprint(professores_app)
app.register_blueprint(coordenador_app)
app.register_blueprint(curso_app)
app.register_blueprint(disciplina_app)
app.register_blueprint(disciplinaofertada_app)
app.register_blueprint(solicitacaomatricula_app)

@app.route('/')
def all():
    return jsonify(database)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
