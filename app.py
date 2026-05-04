from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contacto", methods=["POST"])
def contacto():
    nombre = request.form.get("nombre")
    mensaje = request.form.get("mensaje")

    print(f"Nuevo mensaje: {nombre} - {mensaje}")

    return render_template("index.html", enviado=True)

if __name__ == "__main__":
    app.run()