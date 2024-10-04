from dataclasses import dataclass
from datetime import time

from App.exts import db

@dataclass
class Schedule(db.Model):
    __tablename__ = 'schedule'
    id:int = db.Column(db.Integer, primary_key=True)
    work_name:str = db.Column(db.String(63), nullable=False)
    start_time:time = db.Column(db.Time, nullable=False)
    end_time:time = db.Column(db.Time, nullable=False)
    is_delete:bool = db.Column(db.Boolean, default=False)

    def __init__(self,work_name,start_time,end_time,is_delete=False):
        self.work_name = work_name
        self.start_time = start_time
        self.end_time = end_time
        self.is_delete = is_delete