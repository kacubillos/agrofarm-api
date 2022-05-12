from msilib.schema import Class


class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:cubillos456@localhost:5432/agrofarm_api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SHOW_SQLALCHEMY_LOG_MESSAGES = False

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}