from Model.base import db
from sqlalchemy.orm import relationship

class Engagement(db.Model):
    __tablename__ = 'Engagement'
    engagement_id = db.Column('engagement_id', db.String(30), primary_key=True, nullable=False)

    name = db.Column('name', db.String(200), nullable=False)
    budgeted_hours = db.Column('budgeted_hours', db.BigInteger(), nullable=True)
    expect_hours = db.Column('expect_hours', db.BigInteger(), nullable=True)
    actual_hours = db.Column('actual_hours', db.BigInteger(), nullable=True)
    start_date = db.Column('start_date', db.DateTime, nullable=True)
    finish_date = db.Column('finish_date', db.DateTime, nullable=True)
    last_entry_date = db.Column('last_entry_date', db.DateTime, nullable=True)
    hours_balance = db.Column('hours_balance', db.BigInteger(), nullable=True)
    inactive_days = db.Column('inactive_days', db.BigInteger(), nullable=True)

    