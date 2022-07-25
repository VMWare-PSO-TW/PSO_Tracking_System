from Model.base import db
from sqlalchemy.orm import relationship
from Model.group_member import GroupMember

class Member(db.Model):
    __tablename__ = 'Member'
    member_id = db.Column('member_id', db.BigInteger(), primary_key=True, nullable=False)
    first_name = db.Column('first_name', db.String(20), nullable=False)
    last_name = db.Column('last_name', db.String(20), nullable=False)
    role = db.Column('role', db.String(30), nullable=False)
    employee = db.Column('employee', db.Boolean(), nullable=False)

    # group = relationship('Group', secondary=GroupMember, back_populates='Member')