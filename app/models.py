import datetime

from werkzeug.security import generate_password_hash

from . import db

class Admin(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=True)
    password_encrypted = db.Column(db.String(102), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())

    @property
    def password(self):
        pass

    @password.setter
    def password(self, value):
        self.password_encrypted = generate_password_hash(value)

    @classmethod
    def create_admin(cls, name, email, password):
        admin = Admin(name=name, email=email, password=password)

        db.session.add(admin)
        db.session.commit()

        return admin

    @classmethod
    def get_by_id(cls, id):
        return Admin.query.filter_by(id=id).first()

    @classmethod
    def update_admin(cls, id, name, email):
        admin = Admin.get_by_id(id)

        if admin is None:
            return False

        admin.name = name
        admin.email = email

        db.session.commit()

        return admin

    @classmethod
    def delete_admin(cls, id):
        admin = Admin.get_by_id(id)

        if admin is None:
            return False

        db.session.delete(admin)
        db.session.commit()

        return admin