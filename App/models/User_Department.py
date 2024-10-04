# from flask_sqlalchemy import SQLAlchemy
#
#
# db = SQLAlchemy()
# # 定义关联表，存储用户和角色的关联信息
# user_department = db.Table('user_department',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
#     db.Column('department_id', db.Integer, db.ForeignKey('department.id'), primary_key=True)
# )
from dataclasses import dataclass
from App.exts import db

@dataclass
class UserDepartment(db.Model):
    __tablename__ = 'user_department'
    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    department_id: int = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    role : int = db.Column(db.Integer, nullable=True)

    def __init__(self, user_id, department_id, role=None):
        self.user_id = user_id
        self.department_id = department_id
        self.role = role