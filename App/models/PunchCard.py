from dataclasses import dataclass
from datetime import date, datetime, time
from App.exts import db

@dataclass
class PunchCard(db.Model):
    __tablename__ = 'punch_card'
    id :int = db.Column(db.Integer, primary_key=True)
    user_id:int = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    clock_date :date = db.Column(db.Date, default=datetime.now, nullable=True)
    clock_time : time = db.Column(db.Time, default=datetime.now, nullable=True)
    location :str = db.Column(db.String(255), nullable=True)
    photo :str = db.Column(db.String(255), nullable=True)
    department_id :int = db.Column(db.Integer, db.ForeignKey('department.id'),nullable=False)

    def __init__(self, user_id,department_id, clock_date=None, location=None, photo=None):
        self.user_id = user_id
        self.department_id = department_id
        if clock_date:self.clock_date = clock_date
        if location:self.location = location
        if photo:self.photo = photo
