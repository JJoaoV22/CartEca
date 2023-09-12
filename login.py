from flask import Flask, render_template, request, redirect
from carta import enviar
app = Flask(__name__)

@app.route('/')

def hello_agendeca():
    return render_template("login.html")

@app.route("/", methods = ["POST"])
def login():
    if request.method == "POST":
        nome = request.form.get("nome")
        senha = request.form.get("senha")
        if nome == "tiquinho" and senha== "tiquinho":
            return redirect("/carta")
        else:
            return "<h1>Senha ou Login inválidos</h1>"


@app.route('/carta')

def enviar():
    desti = request.form.get("destinatario")
    data = request.form.get("data")
    mens = request.form.get("mensagem")
    reme = request.form.get("remetente")
    if request.method == "POST":
        enviar(desti,data,mens)
    return render_template("index.html")

app.run()