
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 定义关联表，存储用户和角色的关联信息
user_department = db.Table('user_department',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('department_id', db.Integer, db.ForeignKey('department.id'), primary_key=True)
)
