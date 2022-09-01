from calendar import SATURDAY
from sqlalchemy import ForeignKey
from Model.base import db


class ForecastHours(db.Model):
    __tablename__ = 'ForecastHours'
    member_name = db.Column('member_name', db.String(30), primary_key=True, nullable=False)
    member_id = db.Column('member_id',  db.BigInteger(), primary_key=True, nullable=False)
    engagement_name = db.Column('engagement_name', db.String(30), primary_key=True, nullable=False)
    Saturday = db.Column('Saturday', db.BigInteger(), nullable=True)
    Sunday = db.Column('Sunday', db.BigInteger(), nullable=True)
    Monday = db.Column('Monday', db.BigInteger(), nullable=True)
    Tuesday = db.Column('Tuesday',  db.BigInteger(), nullable=True)
    Wednesday = db.Column('Wednesday', db.BigInteger(), nullable=True)
    Thursday = db.Column('Thursday', db.BigInteger(), nullable=True)
    Friday = db.Column('Friday', db.BigInteger(), nullable=True)

    def __init__(self, Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday):
        self.Saturday = Saturday
        self.Sunday = Sunday
        self.Monday = Monday
        self.Tuesday = Tuesday
        self.Wednesday = Wednesday
        self.Thursday = Thursday
        self.Friday = Friday