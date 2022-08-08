from flask import jsonify, request, Blueprint, Response, render_template, redirect, url_for
from Model.phase import Phase
from Model.group_member import GroupMember
from Model.member import Member
from Model.base import db


phases = Blueprint('phases', __name__)


@phases.route('/<string:engagement_id>', methods=['GET'])
def list(engagement_id):

    objects = Phase.query.filter_by(engagement_id=engagement_id)
    
    phaseList = []

    for o in objects:
        phaseList.append({
                'name': o.name,
                'step': o.step,
                'expect': o.expect_hours,
                'actual': o.actual_hours,
                'start_date': o.start_date if o.start_date else None,
                'end_date': o.end_date if o.end_date else None
        })


    totalSteps = len(phaseList)

    memberList = []
    memberSet = set()

    for i in range(totalSteps):

        phase = Phase.query.filter_by(engagement_id=engagement_id).filter_by(step=i + 1).first()
        groupMembers = GroupMember.query.filter_by(group_id=phase.group_id).all()

        for gp in groupMembers:
            member = Member.query.filter_by(member_id=gp.member_id).first()
            name = f'{member.first_name} {member.last_name}'
            role = member.role
            if name not in memberSet:
                memberList.append({
                    'name': name,
                    'role': role
                })
                memberSet.add(f'{member.first_name} {member.last_name}')

    phaseList.sort(key=lambda x:x['step'])
    
    response = jsonify({
        'phases': phaseList,
        'members': memberList
    })

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
                'actual': phase.actual_hours,
                'start_date': phase.start_date if phase.start_date else None,
                'end_date': phase.end_date if phase.end_date else None},

        'members': groupMembersList
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
    
