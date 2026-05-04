from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        "id": 1,
        "titulo": "Proyecto 1",
        "descripcion": "Descripción del proyecto",
        "imagen": "img1.jpg"
    },
    {
        "id": 2,
        "titulo": "Proyecto 2",
        "descripcion": "Otro trabajo realizado",
        "imagen": "img2.jpg"
    }
]

@app.route("/")
def home():
    return render_template("index.html", posts=posts)

@app.route("/post/<int:id>")
def post(id):
    post = next((p for p in posts if p["id"] == id), None)
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)