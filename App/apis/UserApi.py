from flask import request
from flask_restful import Resource
from App.common.ErrorCode import ErrorCode
from App.common.RequestUtils import RequestUtils
from App.exception.BusinessException import BusinessException
from App.exts import db
from App.common.ResultUtils import *
from App.models.Userold import User


class AddUser(Resource):
    def post(self):
        json = request.json
        if json is None or len(json) == 0 or RequestUtils.is_blank(json,'name')  or RequestUtils.is_blank(json,'role') or RequestUtils.is_blank(json,'identification'):
            raise BusinessException(ErrorCode.PARAMS_ERROR, '参数错误')
        name = request.json.get('name')
        role = request.json.get('role')
        identification = request.json.get('identification')
        if User.query.filter_by(identification=identification).count() > 0: raise BusinessException(ErrorCode.PARAMS_ERROR,'该用户已存在!')
        department = None
        avatar = None
        score = None
        captainId = None
        if not RequestUtils.is_blank(json,'department'): department = request.json.get('department')
        if not RequestUtils.is_blank(json,'avatar'): avatar = request.json.get('avatar')
        if not RequestUtils.is_blank(json,'captainId'): captainId = request.json.get('captainId')
        if not RequestUtils.is_blank(json,'score'): score = request.json.get('score')
        user = User(name=name,role=role,identification=identification,department=department,captainId=captainId,score=score,avatar=avatar)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
        return ResultUtils.success(user, 'ok')


class UpdateUser(Resource):
    def post(self):
        json = request.json
        if json is None or len(json) == 0 or RequestUtils.is_blank(json,'id') or int(json.get('id')) <= 0: raise BusinessException(ErrorCode.PARAMS_ERROR)
        user_id = json.get('id')
        user = User.query.get(user_id)
        if user is None: raise BusinessException(ErrorCode.NOT_FOUND_ERROR)
        for key in json.keys():
            if key == 'id': continue
            if key == 'identification':
                if User.query.filter_by(identification=json.get('identification')).count() > 0:
                    raise BusinessException(
                    ErrorCode.PARAMS_ERROR, '该用户已存在!')
            setattr(user, key, json[key])
        db.session.commit()
        return ResultUtils.success(user)

class GetUser(Resource):
    def get(self):
        args = request.args
        print(args)
        if RequestUtils.is_not_valid(args,'id'): raise BusinessException(ErrorCode.PARAMS_ERROR)
        id = args.get('id')
        user = User.query.get(id)
        if user is None: raise BusinessException(ErrorCode.NOT_FOUND_ERROR)
        return ResultUtils.success(user)

class GetUserList(Resource):
    def get(self):
        user_list = User.query.all()
        return ResultUtils.success(user_list)

class DeleteUser(Resource):
    def get(self):
        args = request.args
        if RequestUtils.is_not_valid(args,'id'): raise BusinessException(ErrorCode.PARAMS_ERROR)
        id = args.get('id')
        user = User.query.get(id)
        if user is None: raise BusinessException(ErrorCode.NOT_FOUND_ERROR)

        try:
            db.session.delete(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
        return ResultUtils.success(None,'删除成功')