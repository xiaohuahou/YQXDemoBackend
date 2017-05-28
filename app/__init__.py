# coding=utf-8
from flask import Flask

from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # 注册蓝本
    # 增加auth蓝本
    from app.users import users as users_blueprint
    app.register_blueprint(users_blueprint, url_prefix='/users')

    # 附加路由和自定义的错误页面

    return app