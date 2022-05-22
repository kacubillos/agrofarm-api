from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

from dotenv import load_dotenv

app = Flask(__name__)

db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()

from .routes import page
from .models import Admin

def create_app(config):
    load_dotenv()

    app.config.from_object(config)

    app.register_blueprint(page)

    with app.app_context():
        jwt.init_app(app)
        db.init_app(app)
        ma.init_app(app)
        db.create_all()

    return app