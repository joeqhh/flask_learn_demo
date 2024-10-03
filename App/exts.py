from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from App.exception.BusinessException import BusinessException
from werkzeug.exceptions import HTTPException

db = SQLAlchemy()


class Api(Api):
    def handle_error(self, e):
        if isinstance(e, HTTPException):
            raise HTTPException()
        if isinstance(e, BusinessException):
            raise BusinessException(e)
        else:
            Exception(e)

api = Api()# 调用自定义的Api去路由分发


def init_exts(app):
    db.init_app(app=app)
    api.init_app(app=app)