import os
import psycopg2

from Model.base import db
from Model.engagement import Engagement
from Model.phase import Phase
from Model.group_member import GroupMember
from Model.group import Group
from Model.member import Member

db.create_all()