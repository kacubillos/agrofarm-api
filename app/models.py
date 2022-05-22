import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from . import db

class UserBaseModel:
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

    def verify_password(self, password):
        return check_password_hash(self.password_encrypted, password)

    @classmethod
    def create_element(cls, name, email, password):
        user = cls(name=name, email=email, password=password)

        db.session.add(user)
        db.session.commit()

        return user

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def update_element(cls, id, name, email):
        user = cls.get_by_id(id)

        if user is None:
            return False

        user.name = name
        user.email = email

        db.session.commit()

        return user

    @classmethod
    def delete_element(cls, id):
        user = cls.get_by_id(id)

        if user is None:
            return False

        db.session.delete(user)
        db.session.commit()

        return user

class Admin(UserBaseModel, db.Model):
    __tablename__ = 'admins'

    articles = db.relationship('Article')

class Farmer(UserBaseModel, db.Model):
    __tablename__ = 'farmers'

    crops = db.relationship('Crop')

class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(100), nullable=True)
    url_image = db.Column(db.String(), nullable=True)
    content = db.Column(db.Text(), nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('admins.id'))
    published_at = db.Column(db.DateTime, default=datetime.datetime.now())

    @classmethod
    def create_article(cls, title, description, url_image , content, author_id):
        article = Article(title=title, description=description, url_image=url_image , content=content, author_id=author_id)

        db.session.add(article)
        db.session.commit()

        return article

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def update_article(cls, id, title, description, url_image, content, author_id):
        user = cls.get_by_id(id)

        if user is None:
            return False

        user.title = title
        user.description = description
        user.url_image = url_image
        user.content = content
        user.author_id = author_id

        db.session.commit()

        return user

    @classmethod
    def delete_article(cls, id):
        user = cls.get_by_id(id)

        if user is None:
            return False

        db.session.delete(user)
        db.session.commit()

        return user

class Crop(db.Model):
    __tablename__ = 'crops'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=True)
    crop_type = db.Column(db.String(30), nullable=True)
    seedtime = db.Column(db.DateTime)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmers.id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())

    @classmethod
    def create_crop(cls, title, crop_type, seedtime, farmer_id):
        crop = Crop(title=title, crop_type=crop_type, seedtime=seedtime, farmer_id=farmer_id)

        db.session.add(crop)
        db.session.commit()

        return crop

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def update_crop(cls, id, title, crop_type, seedtime, farmer_id):
        crop = cls.get_by_id(id)

        if crop is None:
            return False

        crop.title = title
        crop.crop_type = crop_type
        crop.seedtime = seedtime
        crop.farmer_id = farmer_id

        db.session.commit()

        return crop

    @classmethod
    def delete_crop(cls, id):
        user = cls.get_by_id(id)

        if user is None:
            return False

        db.session.delete(user)
        db.session.commit()

        return user