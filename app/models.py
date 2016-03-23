from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from . import db, login_manager
from datetime import datetime
from flask.ext.moment import Moment
from markdown import markdown
import bleach


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    head = db.Column(db.String(64),index=True)
    tag = db.Column(db.String(64),index=True)
    body_html = db.Column(db.Text)

    @staticmethod
    def on_change_body(target, value, oldvalue, initiator):
        allowed_tags=['a', 'abbr', 'acronym', 'b',
                      'blockquote', 'code', 'em',
                      'i', 'li', 'ol', 'pre',
                      'strong', 'ul', 'h1',
                      'h2', 'h3', 'p', 'img']
        allowed_attrs = {'img': ['src', 'alt']}
        target.body_html = bleach.linkify(bleach.clean(
            markdown(value, output_format='html'),
            tags=allowed_tags,
            attributes=allowed_attrs,
            strip=True
        ))

db.event.listen(Post.body, 'set', Post.on_change_body)
