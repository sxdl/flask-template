import os
from flask import Flask
from .config import config


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # print(app.root_path)

    # 注册蓝本
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
