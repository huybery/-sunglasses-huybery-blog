# coding=utf-8
# author=huybery
"""
api 接口
"""
from flask import jsonify
from flask import request

from app import blog
from app.models import User

import sys
print(sys.path)

@blog.route("/api/test")
def test_api():
	response = {
		'testNumber': 666
	}
	return jsonify(response)

@blog.route("/api/user", methods=["POST"])
def new_user():
	data = request.get_json()
	user = User()
	user.username = data.get('username')
	user.password = data.get('password')
	user.save()
	return jsonify("ok")