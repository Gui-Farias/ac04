from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1> Olá Mundo! </h1>"

@app.route("/jinja2")
def index_template():
    return render_template("index.html", hello="Olá Mundo!")

@app.route("/get_teste", methods=["GET"])
def get_teste():
    primeiro = request.args.get("primeiro", "primeiro padrao ...")
    segundo = request.args.get("segundo")
    # sim, possu reutilizar...
    return render_template("form_teste.html", primeiro=primeiro, segundo=segundo)

@app.route("/form_teste", methods=["PUT", "POST"])
def form_teste():
    primeiro = request.form["primeiro"]
    segundo = request.form["segundo"]
    # sim, possu reutilizar...
    return render_template("form_teste.html", primeiro=primeiro, segundo=segundo)