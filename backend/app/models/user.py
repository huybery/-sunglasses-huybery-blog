from app import db
from passlib.apps import custom_app_context

class User(db.Document):
    username = db.StringField(require=True)
    password = db.StringField(require=True)

    def hash_password(self, password):
        self.password = custom_app_context.encrypt(password)
        return self.password

    def verify_password(self, password):
        return custom_app_context.verify(password, self.password)