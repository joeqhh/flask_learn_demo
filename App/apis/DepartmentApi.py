from datetime import date

from flask import request
from flask_restful import Resource
from App.common.ErrorCode import ErrorCode
from App.common.RequestUtils import RequestUtils
from App.exception.BusinessException import BusinessException
from App.exts import db
from App.common.ResultUtils import *
from App.models.Department import Department


class AddDepartment(Resource):
    def post(self):
        json = request.json
        if json is None or len(json) == 0 or RequestUtils.is_blank(json,'name'):
            raise BusinessException(ErrorCode.PARAMS_ERROR, '参数错误')
        name = request.json.get('name')
        parent_id = request.json.get('parent_id')
        if Department.query.filter(
                Department.name == name,
                Department.is_delete == 0
        ).count() > 0: raise BusinessException(ErrorCode.PARAMS_ERROR,'该部门已存在!')
        department = Department(name=name,parent_id=parent_id)
        try:
            db.session.add(department)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
        return ResultUtils.success(department, 'ok')


class UpdateDepartment(Resource):
    def post(self):
        json = request.json
        if json is None or len(json) == 0 or not RequestUtils.id_is_valid(json,'id'): raise BusinessException(ErrorCode.PARAMS_ERROR)
        department_id = json.get('id')
        department = Department.query.filter(
            Department.id == department_id,
            Department.is_delete == 0
        ).first()
        if department is None: raise BusinessException(ErrorCode.NOT_FOUND_ERROR)
        for key in json.keys():
            if key == 'id': continue
            if key == 'name':
                other_department = Department.query.filter(
                    Department.name == json.get('name'),
                    Department.is_delete == 0
                ).first()
                if other_department is not None and other_department.id != department_id:
                    raise BusinessException(
                    ErrorCode.PARAMS_ERROR, '该部门已存在!')
            setattr(department, key, json[key])
        db.session.commit()
        return ResultUtils.success(department)

class GetDepartment(Resource):
    def get(self):
        args = request.args
        if not RequestUtils.id_is_valid(args,'id'): raise BusinessException(ErrorCode.PARAMS_ERROR)
        department_id = args.get('id')
        department = Department.query.filter(
            Department.id == department_id,
            Department.is_delete == 0
        ).first()
        if department is None: raise BusinessException(ErrorCode.NOT_FOUND_ERROR)
        return ResultUtils.success(department)


class GetDepartmentList(Resource):
    def get(self):
        department_list = Department.query.filter(Department.is_delete==0).all()
        return ResultUtils.success(department_list)

class DeleteDepartment(Resource):
    def get(self):
        args = request.args
        if not RequestUtils.id_is_valid(args,'id'): raise BusinessException(ErrorCode.PARAMS_ERROR)
        department_id = args.get('id')
        department = Department.query.filter(
            Department.id == department_id,
            Department.is_delete == 0
        ).first()
        if department is None: raise BusinessException(ErrorCode.NOT_FOUND_ERROR)
        department.is_delete = 1
        db.session.commit()
        return ResultUtils.success(None,'删除成功')