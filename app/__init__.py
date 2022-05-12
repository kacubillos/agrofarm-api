from flask import Flask

app = Flask(__name__)

from .routes import page

def create_app(config):
    app.config.from_object(config)

    app.register_blueprint(page)
    return app