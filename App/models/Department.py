from dataclasses import dataclass

from App import db
from App.models.User_Department import user_department


@dataclass
class Department(db.Model):
    __tablename__ = 'department'
    id:int = db.Column(db.Integer, primary_key=True)
    name:str = db.Column(db.String(63), nullable=False)
    parent_id:int = db.Column(db.Integer,nullable=False)
    is_delete:bool = db.Column(db.Boolean, default=False)

    def __init__(self,name,parent_id):
        self.name = name
        self.parent_id = parent_id
        self.is_delete = False
