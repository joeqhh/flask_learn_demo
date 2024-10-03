import datetime

import jwt
from envs.dbgpt_env.Tools.scripts.mailerdaemon import ErrorMessage
from flask import jsonify, session

from App.common.ErrorCode import ErrorCode
from App.common.UserConstant import UserConstant
from App.exception.BusinessException import BusinessException
from App.models.Userold import User


class RequestUtils:
    @staticmethod
    def is_blank(json,key):
        return not json.__contains__(key) or len(json.get(key).strip()) == 0

    @staticmethod
    def is_not_valid(args,key):
        if args is None or args.__len__() == 0 or not args.__contains__(key) or int(args.get(key)) <= 0: return True
        return False

    @staticmethod
    # 生成 JWT Token 的函数
    def generate_token(username,role,time=30):
        # 定义 token 的有效期，这里设置为 30 分钟
        expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=time)
        # 生成 JWT Token
        token = jwt.encode({
            'username': username,
            'role': role,
            'exp': expiration  # 过期时间
        }, 'your_secret_key', algorithm="HS256")
        return token

    @staticmethod
    def decode_token(token,secret_key):
        try:
            token = token.split(" ")[1]  # "Bearer token_value"
            data = jwt.decode(token,secret_key, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            # return jsonify({'message': 'Token has expired!'}), 401
            raise BusinessException(ErrorCode.NOT_LOGIN_ERROR,'token已过期')
        except jwt.InvalidTokenError:
            # return jsonify({'message': 'Invalid Token!'}), 401
            raise BusinessException(ErrorCode.PARAMS_ERROR,'非法token')

    @staticmethod
    def get_login_user():
        login_user = session[UserConstant.USER_LOGIN_STATE.value]
        if RequestUtils.is_not_valid(login_user,'id') : raise BusinessException(ErrorCode.NOT_LOGIN_ERROR)
        id = login_user['id']
        current_user = User.query.get(id)
        if current_user is None: raise BusinessException(ErrorCode.NOT_LOGIN_ERROR)
        return current_user