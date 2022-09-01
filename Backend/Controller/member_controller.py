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


@members.route("/<int:member_id>", methods=['GET'])
def member_engagements(member_id):

    member_info = []
    engagement_list = []

    member = Member.query.filter_by(member_id=member_id).first()

    engagements_by_member = GroupMember.query.filter_by(member_id=member_id).all()

    total_expect_hours = 0
    total_actual_hours = 0

    eng_id = set()

    for task in engagements_by_member:
        total_expect_hours += task.expect_hours
        total_actual_hours += task.actual_hours

        if task.engagement_id not in eng_id:
            eng_id.add(task.engagement_id)

    for eng in eng_id:

        phases = GroupMember.query.filter_by(engagement_id=eng).filter_by(member_id=member_id)

        eng_actual_hours = 0
        eng_expect_hours = 0

        for phase in phases:
            eng_actual_hours += phase.actual_hours
            eng_expect_hours += phase.expect_hours

        engagement = Engagement.query.filter_by(engagement_id=eng).first()

        engagement_list.append({
            'id': eng,
            'name': engagement.name,
            'total_expect': eng_expect_hours,
            'total_actual': eng_actual_hours
        })    


    member_info.append({
        'member_id': member.member_id,
        'member_name': member.first_name + " " + member.last_name,
        'role': member.role,
        'total_expect': total_expect_hours,
        'total_actual': total_actual_hours,
        'engagements': engagement_list
    })

    return jsonify(member_info)
