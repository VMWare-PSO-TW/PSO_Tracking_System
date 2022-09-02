from flask import jsonify, request, Blueprint, Response, render_template, redirect, url_for
from Model.phase import Phase
from Model.group_member import GroupMember
from Model.member import Member
from Model.base import db


phases = Blueprint('phases', __name__)


@phases.route("/<string:engagement_id>", methods=['GET'])
def list(engagement_id):

    groupMembers = GroupMember.query.filter_by(engagement_id=engagement_id).all()

    Member_Info = []

    exist_member_list = set()
    #traverse all the tasks in an engagement
    for group_member in groupMembers:

        if group_member.member_id in exist_member_list:
            continue

        member = Member.query.filter_by(member_id=group_member.member_id).first()
        #get all the phases of a particular member
        member_phase_list = GroupMember.query.filter_by(member_id=group_member.member_id,
            engagement_id=group_member.engagement_id).all()

        total_actual_hours = 0
        total_expect_hours = 0

        for hours in member_phase_list:
            total_actual_hours += hours.actual_hours
            total_expect_hours += hours.expect_hours

        phase_list = []

        for phase in member_phase_list:
            phase_list.append({
                'step': int(phase.group_id[-1]),
                'actual':phase.actual_hours,
                'expect':phase.expect_hours
            })

        Member_Info.append({
                'id': group_member.member_id,
                'name': member.first_name + " " + member.last_name,
                'role': member.role,
                'total_actual': total_actual_hours,
                'total_expect': total_expect_hours,
                'phases': phase_list
        })
        
        exist_member_list.add(group_member.member_id)

    response = jsonify(
        Member_Info
    )

    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@phases.route('/<string:engagement_id>/<int:step>', methods=['GET'])
def phase(engagement_id, step):

    phase = Phase.query.filter_by(engagement_id=engagement_id).filter_by(step=step).first()

    groupMembers = GroupMember.query.filter_by(group_id=phase.group_id).all()

    groupMembersList = []

    for gp in groupMembers:
        member = Member.query.filter_by(member_id=gp.member_id).first()
        groupMembersList.append({
            'name': f'{member.first_name} {member.last_name}',
            'expect': gp.expect_hours,
            'actual': gp.actual_hours,
            'role': member.role
        })


    response = jsonify({
        'phase': {
                'name': phase.name,
                'step': phase.step,
                'expect': phase.expect_hours,
                'actual': phase.actual_hours},

        'members': groupMembersList
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@phases.route("/<string:engagement_id>/phases_by_engagement", methods=['GET'])
def phases_total_hours(engagement_id):

    phases = Phase.query.filter_by(engagement_id=engagement_id).all()

    hours_by_phase_list = []

    for phase in phases:
        hours_by_phase_list.append({
            'phase': phase.step,
            'expect_hours': phase.expect_hours,
            'actual_hours': phase.actual_hours
        })
    
    sorted(hours_by_phase_list, key=lambda x: x['phase'])

    return jsonify(hours_by_phase_list)