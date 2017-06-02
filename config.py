import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    FLASKY_MAIL_SUBJECT_PREFIX = '[YQXDemo]'
    FLASKY_MAIL_SENDER = 'YQXDemo Admin xiaohua.hou@gmail.com'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_URI = os.environ.get('DEV_DATABASE_URL') or \
        'mongodb://localhost:27017'
    MONGODB_DB = 'dev'

class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    MONGODB_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    MONGODB_DB = 'test'

class ProductionConfig(Config):
    MONGODB_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'prodection': ProductionConfig,

    'default': DevelopmentConfig
}