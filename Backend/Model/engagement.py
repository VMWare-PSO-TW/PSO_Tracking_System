from Model.base import db
from sqlalchemy.orm import relationship

class Engagement(db.Model):
    __tablename__ = 'Engagement'
    engagement_id = db.Column('engagement_id', db.String(30), primary_key=True, nullable=False)

    name = db.Column('name', db.String(200), nullable=False)
    expect_hours = db.Column('expect_hours', db.BigInteger(), nullable=False)
    actual_hours = db.Column('actual_hours', db.BigInteger(), nullable=False)
    internal_hours = db.Column('internal_hours', db.BigInteger(), nullable=True)
    subb_hours = db.Column('subb_hours', db.BigInteger(), nullable=True)
    start_date = db.Column('start_date', db.DateTime, nullable=True)
    end_date = db.Column('end_date', db.DateTime, nullable=True)

    