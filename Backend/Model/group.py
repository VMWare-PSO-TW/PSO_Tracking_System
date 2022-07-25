from sqlalchemy import ForeignKey
from Model.base import db
from sqlalchemy.orm import relationship
from Model.group_member import GroupMember

class Group(db.Model):
    __tablename__ = 'Group'
    group_id = db.Column('group_id', db.String(30), primary_key=True, nullable=False)
    phase_id = db.Column('phase_id', db.String(30), nullable=False)

    internal_hours = db.Column('internal_hours', db.BigInteger(), nullable=True)
    subb_hours = db.Column('subb_hours', db.BigInteger(), nullable=True)

    # phase = relationship('Phase', back_populates='Group')
    # member = relationship('Member', secondary=GroupMember, back_populates='Group')