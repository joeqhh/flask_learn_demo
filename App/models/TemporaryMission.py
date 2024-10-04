from dataclasses import dataclass
from datetime import time

from App.exts import db

@dataclass
class TemporaryMission(db.Model):
    __tablename__ = 'temporary_mission'
    id:int = db.Column(db.Integer, primary_key=True)
    mission_name:str = db.Column(db.String(127), nullable=False)
    description:str = db.Column(db.String(510),nullable=True)
    start_time:time = db.Column(db.Time,nullable=False)
    end_time:time = db.Column(db.Time,nullable=False)
    creator_id:int = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=True)
    is_later:bool = db.Column(db.Boolean,nullable=True)
    is_deleted:bool = db.Column(db.Boolean,nullable=True,default=False)

    def __init__(self,mission_name,start_time,end_time,description=None,creator_id=None,is_later=None,is_deleted=False):
        self.mission_name = mission_name
        self.start_time = start_time
        self.end_time = end_time
        self.description = description
        self.creator_id = creator_id
        self.is_later = is_later
        self.is_deleted = is_deleted
