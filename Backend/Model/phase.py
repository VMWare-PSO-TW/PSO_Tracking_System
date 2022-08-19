from sqlalchemy import ForeignKey
from Model.base import db
from sqlalchemy.orm import relationship



class Phase(db.Model):
    __tablename__ = 'Phase'
    phase_id = db.Column('phase_id', db.String(30), primary_key=True, nullable=False)
    engagement_id = db.Column('engagement_id', db.String(30), nullable=False)
    group_id = db.Column('group_id', db.String(30), nullable=False)

    name = db.Column('name', db.String(200), nullable=False)
    step = db.Column('step', db.BigInteger(), nullable=False)
    expect_hours = db.Column('expect_hours', db.BigInteger(), nullable=False)
    actual_hours = db.Column('actual_hours', db.BigInteger(), nullable=False)
    

    # engagement = relationship('Engagement', back_populates='Phase')
    # group = relationship('Group', back_populates='Phase', uselist=False)