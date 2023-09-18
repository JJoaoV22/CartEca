from flask import Flask, render_template, request
from model import enviar

app = Flask(__name__)

@app.route('/')
def hello_agendeca():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        nome = request.form.get("nome")
        senha = request.form.get("senha")
        if nome == "123" and senha == "123":
            return render_template("index.html")
        else:
            return "<h1>Senha ou Login inválidos</h1>"

@app.route('/carta', methods=["POST"])
def carta():
    destinatario = request.form.get("destinatario")
    data = request.form.get("data")
    corpo = request.form.get("corpo")
    remetente = request.form.get("remetente")
    if request.method == "POST":
        enviar(data, remetente, destinatario, corpo)
        return render_template("index.html")

def lsldldls():
    print("hahaha zuei o codigo de vcs")
    
if __name__ == "__main__":
    app.run(debug=True)
