from database import db
from flask_login import UserMixin

# Multiple inheritance for User model
class User(db.Model, UserMixin):
    # id(int):PK, username(string), password(text)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

