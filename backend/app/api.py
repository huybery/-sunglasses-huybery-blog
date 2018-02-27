# coding=utf-8
# author=huybery
"""
api 接口
"""
from flask import jsonify
from flask import request
from flask import abort
from flask import g
from flask import url_for
from flask import make_response

from flask_restful import Api
from flask_restful import Resource
from flask_restful import reqparse

from app import blog
from app import auth
from app.models import User
from app.models import Post

from app.utils import make_public_post

import random

# init restful api
# 初始化 resful api 
api = Api(blog)


@blog.errorhandler(404)
def not_found(error):
	"""
	拦截 404 返回 JSON
	"""
	return make_response(jsonify({'error': 'Not found'}), 404)


@blog.route('/api/test')
def test_api():
	response = {
		'testNumber': random.randint(0, 100)
	}
	return jsonify(response)


@blog.route('/api/register', methods=["POST"])
def register_user():
	"""
	注册用户
	"""
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	if username is None or password is None:
		# missing auguments
		abort(400)
	if len(User.objects(username=username)) > 0:
		# existing user
		abort(400)
	user = User()
	user.username = username
	user.hash_password(password)
	user.save()
	return jsonify({'username': user.username})


@blog.route('/api/user/<username>')
def user_exist(username):
	response = {
		username: False
	}
	user_list = User.objects(username=username)
	if len(user_list) > 0:
		response[username] = True
	return jsonify(response)


@auth.verify_password
def verify_password(username_or_token, password):
	if request.path == '/api/login':
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


@blog.route('/api/login')
@auth.login_required
def get_auth_token():
	"""
	获取 token
	"""
	token = g.user.generate_auth_token()
	loginUser = g.user.username
	return jsonify({
		'token': token.decode('ascii'),
		'loginUser': loginUser
	})


@blog.route('/api/user', methods=['GET'])
@auth.login_required
def get_user_list():
	"""
	获取所有用户列表
	"""
	response = []
	for user in User.objects():
		user_info = {
			"uid": str(user.id),
			"username": user.username,
			"password": "**********"
		}
		response.append(user_info)
	return jsonify(response)


@blog.route('/api/user/<uid>', methods=['DELETE', 'PUT'])
@auth.login_required
def rest_user(uid):
	"""
	CUDR User
	"""
	def _del_user(uid):
		"""
		根据 uid 删除用户
		"""
		user = User.objects(id=uid)[0]
		username = user.username
		user.delete()
		response = {
			"username": username,
			"type": "delete",
			"err_code": 0
		}
		return jsonify(response)

	def _put_user(uid):
		"""
		根据 uid 修改用户的 username, password
		"""
		user = User.objects(id=uid)[0]
		data = request.get_json()
		if 'username' in data:
			if len(User.objects(username=data.get('username'))) > 0:
				response = {
					"type": "put",
					"err_code": 1
				}
				return jsonify(response)
			else:
				user.username = data.get('username')
		elif 'password' in data:
			user.hash_password(data.get('password'))
		username = user.username
		user.save()
		response = {
			"username": username,
			"type": 'put',
			"err_code": 0
		}
		return jsonify(response)
	if request.method == 'DELETE':
		return _del_user(uid)
	elif request.method == 'PUT':
		return _put_user(uid)


class PostListAPI(Resource):
	"""
	文章列表 API
	"""
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument(
			'title', 
			type=str, 
			required=True,
			help='No post title provided',
			location=['json', 'args']
		)
		self.reqparse.add_argument(
			'body',
			type=str,
			default='',
			help='No post body provided',
			location=['json', 'args']
		)
		super(PostListAPI, self).__init__()

	def get(self):
		"""
		获取文章列表
		"""
		response = []
		for post in Post.objects:
			post_info = {
				"id": str(post.id),
				"title": post.title,
			}
			# ids => uri
			post_info = make_public_post(post_info)
			response.append(post_info)
		# flask restful 自动将 response 序列化为 json， 所以无需 jsonify
		return response
	
	def post(self):
		"""
		增加文章
		"""
		args = self.reqparse.parse_args()
		title = args.get('title')
		body = args.get('body')
		post = Post(title=title, body=body)
		post.add_views(init=True)
		post.save()
		return post.get_dict(), 201

	
class PostAPI(Resource):
	"""
	文章 API 根据 id 获取、更改、删除文章
	"""
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument(
			'title', 
			type=str, 
			required=True,
			help='No post title provided',
			location=['json', 'args']
		)
		self.reqparse.add_argument(
			'body',
			type=str,
			default='',
			help='No post body provided',
			location=['json', 'args']
		)
		super(PostAPI, self).__init__()

	def get(self, id):
		pass

	def put(self, id):
		pass

	def delete(self, id):
		pass

api.add_resource(PostListAPI, '/api/v1/posts', endpoint='posts')
api.add_resource(PostAPI, '/api/v1/post/<id>', endpoint='post')
