from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_admin import Admin
from flask_babelex import Babel

from config import config

db = SQLAlchemy()
admin = Admin(name="My Love")
bootstrap = Bootstrap()
babel = Babel()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    bootstrap.init_app(app)
    admin.init_app(app)
    babel.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .vote import vote as vote_blueprint
    app.register_blueprint(vote_blueprint, url_prefix='/vote')

    from .love import love as love_blueprint
    app.register_blueprint(love_blueprint, url_prefix="/love")

    @app.after_request
    def after_request(response):
        print "after_request"
        return response

    return app

