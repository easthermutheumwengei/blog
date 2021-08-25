import os


class Config:
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'estherkey'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://esther:1234@localhost/blog'
    DEBUG = False


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
