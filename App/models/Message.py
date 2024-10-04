from dataclasses import dataclass

from App.exts import db

@dataclass
class Message(db.Model):
    __tablename__ = 'message'

    id :int = db.Column(db.Integer, primary_key=True)
    message :str = db.Column(db.String(510))
    sender :str = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    receiver :str = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    log_id :int = db.Column(db.Integer,db.ForeignKey('reward_punish_log.id'),nullable=True)
    is_read :bool = db.Column(db.Boolean, default=False)

    def __init__(self,sender,receiver,message=None,log_id=None,is_read=False):
        self.sender = sender
        self.receiver = receiver
        self.is_read = is_read
        if log_id:self.log_id = log_id
        if message :self.message = message
