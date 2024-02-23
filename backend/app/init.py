# 役割：Flask アプリケーションのインスタンスを作成し、設定する。

from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

def create_app():
    app = Flask(__name__)

    from .routes import main
    app.register_blueprint(main)

    SWAGGER_URL = '/swagger'
    API_URL = '/static/openapi.yml'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL, API_URL, config={'app_name': "ToDoアプリ"}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app
