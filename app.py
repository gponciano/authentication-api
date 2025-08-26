from flask import Flask, request, jsonify
from database import db
from models.user import User
from flask_login import LoginManager, login_user, current_user, logout_user, login_required


app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

login_manager = LoginManager()
# Initiating instance for the class, SQLAlchemy is the class whereas app is the instance
db.init_app(app)
login_manager.init_app(app)


login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
     return User.query.get(user_id)
     
# Login view
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
                login_user(user)
                print(current_user.is_authenticated)
                return jsonify({"message": "Login Succesful"})

    return jsonify({"message": "Invalid Credentials"}), 400

# Logout view
@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout succesfully"})

@app.route("/user", methods=["POST"])
@login_required
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
         user = User(username=username, password=password)
         db.session.add(user)
         db.session.commit()
         return jsonify({"message": "User registered sucessfully"})
    return jsonify({"message": "Invalid user details"}), 401

@app.route("/hello-world", methods=["GET"])
def hello_world():
    return "hello world"

if __name__ == '__main__':
    app.run(debug=True)

# db connect: flask shell
# sqlite viewer extension is needed
