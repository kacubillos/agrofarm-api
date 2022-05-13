from marshmallow import fields

from . import ma

class AdminSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    email = fields.String()
    password_encrypted = fields.String()
    created_at = fields.DateTime()
    articles = fields.Nested('ArticleSchema', many=True)

    class Meta:
        ordered = True

class FarmerSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    email = fields.String()
    password_encrypted = fields.String()
    created_at = fields.DateTime()
    crops = fields.Nested('CropSchema', many=True)

    class Meta:
        ordered = True

class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'url_image' , 'content', 'author_id', 'published_at')
        ordered = True

class CropSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'crop_type', 'seedtime', 'farmer_id', 'created_at')
        ordered = True