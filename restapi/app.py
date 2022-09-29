# from flask import Flask, request, json, jsonify, render_template, url_for
from flask import Flask
# import redis
import os
from api import api
import api.config as config
from flask_migrate import Migrate
from api import db


# create_app関数を作成する
def create_app(config_key):
    # Flaskインスタンス生成
    app = Flask(__name__)
    app.config.from_object(config[config_key])

    # SQLAlchemyとアプリを連携する
    db.init_app(app)
    return app


app = create_app('local')
Migrate(app, db)
# blueprintをアプリケーションに登録
app.register_blueprint(api)
