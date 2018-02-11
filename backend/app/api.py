# coding=utf-8
# author=huybery
"""
api 接口
"""
from flask import jsonify
from flask import request
from flask import abort
from flask import g
import random

from app import blog
from app import auth
from app.models import User

@blog.route("/api/test")
def test_api():
	response = {
		'testNumber': random.randint(0, 100)
	}
	return jsonify(response)

@blog.route("/api/register", methods=["POST"])
def register_user():
	"""
	注册用户
	"""
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	if username is None or password is None:
		# missing auguments
		print("missing")
		abort(400)
	if len(User.objects(username=username)) > 0:
		# existing user
		print(User.objects(username=username))
		print("username has exist")
		abort(400)
	user = User()
	user.username = data.get('username')
	user.hash_password(password)
	user.save()
	return jsonify({'username': user.username})

@auth.verify_password
def verify_password(username_or_token, password):
	if request.path == '/api/token':
		# 首次登陆使用用户名密码验证，用于获取 token
		username = username_or_token
		user_list = User.objects(username=username_or_token)
		if len(user_list) == 0:
			return False
		else:
			user = user_list[0]
			if not user.verify_password(password):
				return False
	else:
		# 其他路由使用 token 验证
		token = username_or_token
		user = User.verify_auth_token(token)
		if not user:
			return False
	g.user = user
	return True

@blog.route("/api/token")
@auth.login_required
def get_auth_token():
	"""
	获取 token
	"""
	token = g.user.generate_auth_token()
	return jsonify({'token': token.decode('ascii')})

@blog.route("/api/resource")
@auth.login_required
def get_resouce():
	return jsonify({'data': 'Hello, %s' % g.user.username})

