from App.common.ErrorCode import ErrorCode
from App.exception.BusinessException import BusinessException
from App.models.User_Department import UserDepartment
from App.exts import db

class UserDepartmentService:
    def add_user_department(self, user_id,department_id,role=None):
        from App.models.Department import Department
        department = Department.query.filter(
            Department.id == department_id,
            Department.is_delete == 0
        ).first()
        if department is None: raise BusinessException(ErrorCode.NOT_FOUND_ERROR)
        from App.models.User import User
        user = User.query.filter(
            User.id == user_id,
            User.is_delete == 0
        ).first()
        if user is None: raise BusinessException(ErrorCode.NOT_FOUND_ERROR)
        user_department = UserDepartment(user_id=user_id, department_id=department_id, role=role)
        try:
            db.session.add(user_department)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()

    def delete_user_department(self,user_department_id):
        if user_department_id is None or user_department_id <= 0: raise BusinessException(ErrorCode.PARAMS_ERROR)
        user_department = UserDepartment.query.get(user_department_id)
        if user_department is None: raise BusinessException(ErrorCode.NOT_FOUND_ERROR)
        db.session.delete(user_department)
        db.session.commit()

    def update_user_department(self,user_department_id,new_department_id=None,role=None):
        if new_department_id is None and role is None: pass
