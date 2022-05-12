from flask import Blueprint, jsonify, request

from app.models import Admin
from app.schemas import AdminSchema

admin_schema = AdminSchema()
admins_schema = AdminSchema(many=True)

page = Blueprint('page', __name__)

@page.app_errorhandler(404)
def page_not_found(error):
    return 'No encontrado', 404

@page.route('/')
def index():
    return 'Hola mundo desde views'

@page.route('/api/admins/', methods=['GET', 'POST'])
def admins():
    if request.method == 'POST':
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        admin = Admin.create_admin(name, email, password)
        print('Admin {} creado correctamente'.format(admin.id))
        return admin_schema.jsonify(admin)

    all_admins = Admin.query.all()
    result = admins_schema.dump(all_admins)
    return jsonify(result)

@page.route('/api/admins/<int:admin_id>')
def get_admin(admin_id):
    admin = Admin.query.get_or_404(admin_id)
    return admin_schema.jsonify(admin)

@page.route('/api/admins/<int:admin_id>', methods=['PUT'])
def update_admin(admin_id):
    name = request.json['name']
    email = request.json['email']

    admin = Admin.update_admin(admin_id, name, email)
    return admin_schema.jsonify(admin)

@page.route('/api/admins/<int:admin_id>', methods=['DELETE'])
def delete_admin(admin_id):
    admin = Admin.delete_admin(admin_id)
    return admin_schema.jsonify(admin)