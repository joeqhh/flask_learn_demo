from dataclasses import dataclass
from datetime import time

from App.exts import db

@dataclass
class TemporaryWorker(db.Model):
    __tablename__ = 'temporary_worker'
    id:int = db.Column(db.Integer, primary_key=True)
    mission_id:int = db.Column(db.Integer, db.ForeignKey('temporary_mission.id'),nullable=False)
    user_id:int = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=True)
    is_punch : bool = db.Column(db.Boolean, default=False,nullable=True)

    def __init__(self,mission_id,user_id=None,is_punch=False):
        self.mission_id = mission_id
        self.user_id = user_id
        self.is_punch = is_punch