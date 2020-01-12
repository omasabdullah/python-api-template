from os import environ

class Config():
    DEBUG = False
    TESTING = False
    DATABASE_URL = environ.get('DATABASE_URL', '127.0.0.1')
    DATABASE_PORT = environ.get('DATABASE_PORT', '3306')
    DATABASE_NAME = environ.get('DATABASE_NAME', 'db')
    DATABASE_USER = environ.get('DATABASE_USER', 'root')
    DATABASE_PASSWORD = environ.get('DATABASE_PASSWORD', 'password')

    @property
    def DATABASE_URI(self):
        return f'postgresql://{self.DATABASE_USER}@{self.DATABASE_URL}:{self.DATABASE_PORT}'

class ProductionConfig(Config):
    FLASK_ENV = 'production'

class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True

class TestingConfig(Config):
    FLASK_ENV = 'production'
    TESTING = True
