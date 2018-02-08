from app import db

class User(db.Document):
    username = db.StringField(require=True)
    password = db.StringField(require=True)

