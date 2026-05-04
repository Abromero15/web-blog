from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
app.secret_key = "clave_super_secreta"

login_manager = LoginManager()
login_manager.init_app(app)

# Usuario falso (provisional)
USERS = {
    "admin": "1234"
}

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route("/")
def home():
    return render_template("index.html")

# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]

        if user in USERS and USERS[user] == password:
            login_user(User(user))
            return redirect(url_for("admin"))

    return render_template("login.html")

# ADMIN
@app.route("/admin")
@login_required
def admin():
    return render_template("admin.html")

# LOGOUT
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run()