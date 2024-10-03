from flask import Flask
from .exts import init_exts
from .urls import *



def create_app():
    app = Flask(__name__)

    username = 'root'
    password = 'qihao387387'
    database = 'flask_demo'
    db_url = "mysql+pymysql://{}:{}@localhost:3306/{}".format(username, password, database)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your_secret_key'
    init_exts(app = app)


    return app


