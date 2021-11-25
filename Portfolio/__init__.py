from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def register_blueprint(app):
    from Portfolio.main.routes import main
    app.register_blueprint(main)


def register_extension(app):
   db.init_app(app)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extension(app)
    register_blueprint(app)
    return app