# coding=utf-8
# author=huybery
"""
api 接口
"""
from flask import jsonify
from flask import request
from flask import abort

from app import blog
from app.models import User

@blog.route("/api/test")
def test_api():
	response = {
		'testNumber': 666
	}
	return jsonify(response)

@blog.route("/api/register", methods=["POST"])
def new_user():
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