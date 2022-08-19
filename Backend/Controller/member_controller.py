from flask import jsonify, request, Blueprint, Response, render_template, redirect, url_for
from Model.member import Member
from Model.engagement import Engagement
from Model.group_member import GroupMember

members = Blueprint('members', __name__)


@members.route("/engagement_total_hours", methods=['GET'])
def engagement_hours():

    objects = Engagement.query.all()

    total_expect_hours = 0
    total_actual_hours = 0

    for obj in objects:
        total_expect_hours += obj.expect_hours
        total_actual_hours += obj.actual_hours

    return jsonify({
        'total_expect_hours': total_expect_hours,
        'total_actual_hours': total_actual_hours
    })


@members.route("/member_total_hours", methods=['GET'])
def member_hours():

    members = Member.query.all()
    member_list = []

    for member in members:
        
        engagements_by_member = GroupMember.query.filter_by(member_id=member.member_id)

        total_expect_hours = 0
        total_actual_hours = 0

        for task in engagements_by_member:
            total_expect_hours += task.expect_hours
            total_actual_hours += task.actual_hours

        member_list.append({
            'id': member.member_id,
            'name': member.first_name + " " + member.last_name,
            'total_expect': total_expect_hours,
            'total_actual': total_actual_hours
        })

    return jsonify(member_list)

