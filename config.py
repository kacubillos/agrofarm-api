from datetime import timedelta

import os

class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:cubillos456@localhost:5432/agrofarm_api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SHOW_SQLALCHEMY_LOG_MESSAGES = False

    JSON_SORT_KEYS = False

    JWT_SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}