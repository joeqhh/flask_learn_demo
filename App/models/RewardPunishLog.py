from dataclasses import dataclass
from datetime import date, datetime, time
from App.exts import db

@dataclass
class RewardPunishLog(db.Model):
    __tablename__ = 'reward_punish_log'
    id :int = db.Column(db.Integer, primary_key=True)
    user_id :int = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    rule_id :int = db.Column(db.Integer, db.ForeignKey('reward_punish_rule.id'),nullable=True)
    reason :str = db.Column(db.String(510),nullable=True)
    operator_id :int = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    score :int = db.Column(db.Integer,nullable=True)
    photo :str = db.Column(db.String(255))
    status :int = db.Column(db.Integer,nullable=True)
    is_delete :bool = db.Column(db.Boolean,nullable=True)

    def __init__(self,user_id,rule_id,operator_id,reason=None,score=None,photo=None,status=None,is_delete=False):
        self.user_id = user_id
        self.rule_id = rule_id
        self.operator_id = operator_id
        if reason : self.reason = reason
        if score : self.score = score
        if photo : self.photo = photo
        if status : self.status = status
        if is_delete : self.is_delete = is_delete

