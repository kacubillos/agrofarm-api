from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

db = SQLAlchemy()
ma = Marshmallow()

from .routes import page
from .models import Admin

def create_app(config):
    app.config.from_object(config)

    app.register_blueprint(page)

    with app.app_context():
        db.init_app(app)
        ma.init_app(app)
        db.create_all()

    return app