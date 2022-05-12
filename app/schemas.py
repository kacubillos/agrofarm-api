
from . import ma

class AdminSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password_encrypted', 'created_at')