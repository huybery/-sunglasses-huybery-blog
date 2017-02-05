from flask_sqlalchemy import SQLAlchemy
from passlib.apps import custom_app_context

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(128))

    def hash_password(self, password):
        """
        :param password:
        :return: the hash_password
        """
        self.password_hash = custom_app_context.encrypt(password)

    def verify_password(self, password):
        """
        :param password:
        :return: verify password equal old password
        """
        return custom_app_context.verify(password, self.password_hash)
