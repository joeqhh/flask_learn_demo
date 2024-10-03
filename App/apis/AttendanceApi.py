from flask import request, jsonify
from flask_restful import Resource
from App.common.ErrorCode import ErrorCode
from App.common.RequestUtils import RequestUtils
from App.exception.BusinessException import BusinessException
from App.exts import db
from App.common.ResultUtils import *
from App.models.Attendance import Attendance


class AddAttendance(Resource):
    #todo 重复签到
    def post(self):
        json = request.json
        if json is None or len(json) == 0 or RequestUtils.is_blank(json,'userId')  or RequestUtils.is_blank(json,'spot') :
            raise BusinessException(ErrorCode.PARAMS_ERROR, '参数错误')
        user_id = int(json.get('userId'))
        spot = json.get('spot')
        photo = None
        if RequestUtils.is_blank(json,'photo') : photo = json.get('photo')
        attendance = Attendance(userId=user_id,spot=spot,photo=photo)
        try:
            db.session.add(attendance)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
        return ResultUtils.success(attendance, 'ok')

class GetAttendance(Resource):
    def get(self):
        args = request.args
        if RequestUtils.is_not_valid(args,'userId'): raise BusinessException(ErrorCode.PARAMS_ERROR)
        user_id = args.get('userId')
        attendance = Attendance.query.filter_by(userId=user_id).all()
        if attendance is None or len(attendance) == 0: raise BusinessException(ErrorCode.NOT_FOUND_ERROR)
        return ResultUtils.success(attendance)

class GetAttendanceList(Resource):
    def get(self):
        attendance = Attendance.query.all()
        return ResultUtils.success(attendance)

class DeleteAttendance(Resource):
    def get(self):
        args = request.args
        if RequestUtils.is_not_valid(args,'id'): raise BusinessException(ErrorCode.PARAMS_ERROR)
        id = args.get('id')
        attendance = Attendance.query.get(id)
        if attendance is None: raise BusinessException(ErrorCode.NOT_FOUND_ERROR)
        try:
            db.session.delete(attendance)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
        return ResultUtils.success(None,'删除成功')