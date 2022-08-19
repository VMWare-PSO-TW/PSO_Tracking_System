from sqlalchemy import ForeignKey
from Model.base import db
from sqlalchemy.orm import relationship


class GroupMember(db.Model):
    __tablename__ = 'GroupMember'
    engagement_id = db.Column('engagement_id', db.String(30), primary_key=True, nullable=True)
    group_id = db.Column('group_id', db.String(30), primary_key=True, nullable=False)
    member_id = db.Column('member_id',  db.BigInteger(), primary_key=True, nullable=False)
    phase_name = db.Column('phase_name', db.Text(), primary_key=True, nullable=False)
    expect_hours = db.Column('expect_hours', db.BigInteger(), nullable=False)
    actual_hours = db.Column('actual_hours', db.BigInteger(), nullable=False)