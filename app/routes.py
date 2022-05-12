from flask import Blueprint

page = Blueprint('page', __name__)

@page.app_errorhandler(404)
def page_not_found(error):
    return 'No encontrado', 404

@page.route('/')
def index():
    return 'Hola mundo desde views'