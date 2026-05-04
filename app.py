from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {"titulo": "Proyecto 1", "descripcion": "Mi primer proyecto con Flask"},
    {"titulo": "Proyecto 2", "descripcion": "Aplicación web básica"}
]

@app.route("/")
def home():
    return render_template("index.html", posts=posts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)