from datetime import date

from flask import request
from flask_restful import Resource
from App.common.ErrorCode import ErrorCode
from App.common.RequestUtils import RequestUtils
from App.exception.BusinessException import BusinessException
from App.exts import db
from App.common.ResultUtils import *
from App.models.User import User
from App.models.User_Department import UserDepartment
from App.service.UserDepartmentService import UserDepartmentService


class AddUser(Resource):
    def post(self):
        json = request.json
        if json is None or len(json) == 0 or RequestUtils.is_blank(json,['name','idcard','birthday']):
            raise BusinessException(ErrorCode.PARAMS_ERROR, '参数错误')
        idcard = request.json.get('idcard')
        name = request.json.get('name')
        date_list = request.json.get('birthday').split('-')
        y = int(date_list[0])
        m = int(date_list[1])
        d = int(date_list[2])
        birthday = date(y, m, d)
        if User.query.filter(
                User.idcard == idcard,
                User.is_delete == 0
        ).count() > 0: raise BusinessException(ErrorCode.PARAMS_ERROR,'该用户已存在!')
        gender = json.get('gender')
        entry_date = json.get('entry_date')
        photo = json.get('photo')
        score = json.get('score')
        open_id = json.get('open_id')
        user = User(name=name,gender=gender,entry_date=entry_date,photo=photo,score=score,birthday=birthday,open_id=open_id,idcard=idcard)
        try:
            db.session.add(user)
        except Exception as e:
            db.session.rollback()
        departments = json.get('departments')
        if departments:
            db.session.flush()
            uds =  UserDepartmentService()
            for d in departments:
                uds.add_user_department(user.id,d.get('id'),d.get('role'))
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
        return ResultUtils.success(user, 'ok')


class UpdateUser(Resource):
    def post(self):
        json = request.json
        if json is None or len(json) == 0 or not RequestUtils.id_is_valid(json,'id'): raise BusinessException(ErrorCode.PARAMS_ERROR)
        user_id = json.get('id')
        user = User.query.filter(
            User.id == user_id,
            User.is_delete == 0
        ).first()
        if user is None: raise BusinessException(ErrorCode.NOT_FOUND_ERROR)
        for key in json.keys():
            if key == 'id': continue
            if key == 'idcard':
                other_user = User.query.filter(
                    User.idcard == json.get('idcard'),
                    User.is_delete == 0
                ).first()
                if other_user is not None and other_user.id != user_id:
                    raise BusinessException(
                    ErrorCode.PARAMS_ERROR, '该用户已存在!')
            setattr(user, key, json[key])
        db.session.commit()
        return ResultUtils.success(user)

class GetUser(Resource):
    def get(self):
        args = request.args
        if not RequestUtils.id_is_valid(args,'id'): raise BusinessException(ErrorCode.PARAMS_ERROR)
        id = args.get('id')
        user = User.query.filter(
            User.id == id,
            User.is_delete == 0
        ).first()
        if user is None: raise BusinessException(ErrorCode.NOT_FOUND_ERROR)
        return ResultUtils.success(user)


class GetUserList(Resource):
    def get(self):
        user_list = User.query.filter(User.is_delete==0).all()
        return ResultUtils.success(user_list)

class DeleteUser(Resource):
    def get(self):
        args = request.args
        if not RequestUtils.id_is_valid(args,'id'): raise BusinessException(ErrorCode.PARAMS_ERROR)
        id = args.get('id')
        user = User.query.filter(
            User.id == id,
            User.is_delete == 0
        ).first()
        if user is None: raise BusinessException(ErrorCode.NOT_FOUND_ERROR)
        user.is_delete = 1
        db.session.commit()
        return ResultUtils.success(None,'删除成功')