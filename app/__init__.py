# coding=utf-8
from flask import Flask
from config import config
from database import init_db

def create_app(config_name):
    app = Flask(__name__ + config[config_name].MONGODB_DB)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    init_db(config[config_name])

    # 注册蓝本
    # 增加auth蓝本

    URL_PREFIX = '/api/v1'
    from app.users import users as users_blueprint
    app.register_blueprint(users_blueprint, url_prefix=URL_PREFIX)

    from app.classes import classes as classes_blueprint
    app.register_blueprint(classes_blueprint, url_prefix=URL_PREFIX)

    # 附加路由和自定义的错误页面

    return app