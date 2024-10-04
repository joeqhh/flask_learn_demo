from dataclasses import dataclass
from App.exts import db

@dataclass
class RewardPunishRule(db.Model):
    __tablename__ = 'reward_punish_rule'
    id:int  = db.Column(db.Integer, primary_key=True)
    title:str = db.Column(db.String(127), nullable=True)
    type:int = db.Column(db.Integer, nullable=False)
    description:str = db.Column(db.String(510), nullable=True)
    score:int = db.Column(db.Integer, nullable=False)
    department_id:int = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    is_delete:bool = db.Column(db.Boolean, nullable=True, default=False)

    def __init__(self, type, score, department_id, is_delete=False,title=None,description=None):
        self.type = type
        self.score = score
        self.department_id = department_id
        self.is_delete = is_delete
        if title:self.title = title
        if description: self.description = description
