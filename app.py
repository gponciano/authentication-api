from flask import Flask
from database import db

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"


# Initiating instance for the class, SQLAlchemy is the class whereas app is the instance
db.init_app(app)

@app.route("/hello-world", methods=["GET"])
def hello_world():
    return "hello world"

if __name__ == '__main__':
    app.run(debug=True)

# db connect: flask shell
# sqlite viewer extension is needed
