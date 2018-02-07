from flask import Flask
from flask import render_template
from flask import jsonify
from flask_cors import CORS

# Flask 实例
app = Flask(__name__,
			static_folder = "./dist/static",
			template_folder= "./dist")

# 允许跨域
cors = CORS(app, resource={"/api/*": {"origins": "*"}})

@app.route("/api/test")
def test_api():
	response = {
		'testNumber': 666
	}
	return jsonify(response)

# 所有路由由 vue 接管
@app.route("/", defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
