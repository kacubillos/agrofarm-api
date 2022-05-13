from flask import Blueprint, jsonify, request

from app.models import Admin, Article
from app.schemas import AdminSchema, ArticleSchema

admin_schema = AdminSchema()
article_schema = ArticleSchema()

page = Blueprint('page', __name__)

@page.app_errorhandler(404)
def page_not_found(error):
    return {}, 404

@page.route('/')
def index():
    return 'Hola mundo desde views'

""" ADMINS ROUTES """

@page.route('/api/admins/', methods=['GET', 'POST'])
def admins():
    if request.method == 'POST':
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        admin = Admin.create_element(name, email, password)
        return admin_schema.jsonify(admin), 201

    all_admins = Admin.query.all()
    result = admin_schema.dump(all_admins, many=True)
    return jsonify(result)

@page.route('/api/admins/<int:admin_id>')
def get_admin(admin_id):
    admin = Admin.query.get_or_404(admin_id)
    return admin_schema.jsonify(admin)

@page.route('/api/admins/<int:admin_id>', methods=['PUT'])
def update_admin(admin_id):
    name = request.json['name']
    email = request.json['email']

    admin = Admin.update_element(admin_id, name, email)
    return admin_schema.jsonify(admin)

@page.route('/api/admins/<int:admin_id>', methods=['DELETE'])
def delete_admin(admin_id):
    admin = Admin.delete_element(admin_id)
    return admin_schema.jsonify(admin)

""" ARTICLES ROUTES """

@page.route('/api/articles/')
def get_articles():
    all_articles = Article.query.all()
    result = article_schema.dump(all_articles, many=True)
    return jsonify(result)

@page.route('/api/articles/<int:article_id>')
def get_article(article_id):
    article = Article.query.get_or_404(article_id)
    return article_schema.jsonify(article)

@page.route('/api/articles/', methods=['POST'])
def create_article():
    title = request.json['title']
    content = request.json['content']
    description = request.json['description']
    url_image = request.json['url_image']
    author_id = request.json['author_id']

    article = Article.create_article(title, description, url_image, content , author_id)
    return article_schema.jsonify(article), 201

@page.route('/api/articles/<int:article_id>', methods=['PUT'])
def update_article(article_id):
    title = request.json['title']
    content = request.json['content']
    description = request.json['description']
    url_image = request.json['url_image']
    author_id = request.json['author_id']

    article = Article.update_article(article_id, title, description, url_image, content , author_id)
    return article_schema.jsonify(article)

@page.route('/api/articles/<int:article_id>', methods=['DELETE'])
def delete_article(article_id):
    article = Article.delete_article(article_id)
    return article_schema.jsonify(article)