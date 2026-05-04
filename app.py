from flask import Flask, render_template

app = Flask(__name__)

# Datos de ejemplo (tus trabajos)
posts = [
    {
        "titulo": "Proyecto 1",
        "descripcion": "Este es mi primer trabajo."
    },
    {
        "titulo": "Proyecto 2",
        "descripcion": "Este es otro proyecto realizado."
    }
]

@app.route("/")
def home():
    return render_template("index.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)