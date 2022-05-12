import json
from flask import Blueprint, request

from app.models import Admin
from app.schemas import AdminSchema

adminSchema = AdminSchema()

page = Blueprint('page', __name__)

@page.app_errorhandler(404)
def page_not_found(error):
    return 'No encontrado', 404

@page.route('/')
def index():
    return 'Hola mundo desde views'

@page.route('/api/admins', methods=['GET', 'POST'])
def admins():
    if request.method == 'POST':
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        admin = Admin.create_admin(name, email, password)
        print('Admin {} creado correctamente'.format(admin.id))
        return adminSchema.jsonify(admin)