from flask import Flask


def create_app(config_default, config_instance):
    app = Flask(__name__)
    app.config.from_object(config_default)
    app.config.from_pyfile(config_instance)
    from .models import db
    db.init_app(app)
    from .views import api
    app.register_blueprint(api)
    return app
