from dataclasses import dataclass
from App.exts import db


@dataclass
class Department(db.Model):
    __tablename__ = 'department'
    id:int = db.Column(db.Integer, primary_key=True)
    name:str = db.Column(db.String(63),unique=True, nullable=False)
    parent_id:int = db.Column(db.Integer,nullable=True)
    is_delete:int = db.Column(db.Integer, default=False)
    # users = db.relationship('User', secondary=user_department, backref=db.backref('departments', lazy='dynamic'))

    def __init__(self,name,parent_id=None):
        self.name = name
        self.parent_id = parent_id
        self.is_delete = 0
