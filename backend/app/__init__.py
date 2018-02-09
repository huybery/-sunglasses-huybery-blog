# coding=utf-8
from flask import Flask
from flask import render_template
from flask_cors import CORS
from flask_mongoengine import MongoEngine


# Flask 实例
blog = Flask(__name__,
            instance_relative_config=True,
			static_folder = "../../dist/static",
			template_folder= "../../dist")

# 载入配置
blog.config.from_object('config')
blog.config.from_pyfile('config.py')

# 允许跨域
cors = CORS(blog, resource={"/api/*": {"origins": "*"}})

# 数据库初始化
db = MongoEngine()
db.init_app(blog)

# 所有路由由 vue 接管
@blog.route("/", defaults={'path': ''})
@blog.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
