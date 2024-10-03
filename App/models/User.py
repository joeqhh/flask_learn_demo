from dataclasses import dataclass
from datetime import date, datetime
from App import db
from App.models.User_Department import user_department


@dataclass
class User(db.model):
    __tablename__ = 'user'
    id :int =  db.Column(db.Integer, primary_key=True)
    name : str =  db.Column(db.String(63),  nullable=False)
    idcard :str =  db.Column(db.String(31), unique=True, nullable=False)
    gender: bool = db.Column(db.Boolean,  nullable=True)
    birthday : date = db.Column(db.Date, nullable=False)
    entry_date: datetime = db.Column(db.DateTime, nullable=True)
    photo: str  = db.Column(db.String(255), nullable=True)
    open_id :str = db.Column(db.String(127),  nullable=True)
    score :int = db.Column(db.Integer, nullable=True,default=100)
    update_time:datetime = db.Column(db.DateTime, nullable=True,default=datetime.now())
    is_delete :bool = db.Column(db.Boolean, nullable=True, default=False)
    departments = db.relationship('Department', secondary=user_department, backref=db.backref('users', lazy='dynamic'))

    def __init__(self,name,idcard,birthday,open_id=None,photo=None,entry_date=None,gender=None):
        self.name = name
        self.idcard = idcard
        self.birthday = birthday
        self.is_delete = False
        self.score = 100
        if gender:self.gender = gender
        if entry_date:self.entry_date = entry_date
        if open_id: self.open_id = open_id
        if photo: self.photo = photo

