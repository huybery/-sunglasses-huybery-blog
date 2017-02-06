from flask import request, abort, jsonify, Blueprint, g
from flask_httpauth import HTTPBasicAuth
from .models import db, User

auth = HTTPBasicAuth()

api = Blueprint('api', __name__)


@api.route('/api/users', methods=['POST'])
def get_user():
    username = request.json.get('userName')
    password = request.json.get('passWord')
    if username is None or password is None:
        abort(400)
    if User.query.filter_by(username=username).first() is not None:
        abort(400)
    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'username': user.username}), 201


@auth.verify_password
def verify_password(username_or_token, password):
    user = User.verify_auth_token(username_or_token)
    if not user:
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


@api.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration': 600})


@api.route('/api/admin')
@auth.login_required
def admin():
    return jsonify({'data': 'Hello, %s' % g.user.username})
