from urllib import response
from flask import jsonify, request, Blueprint, Response, render_template, redirect, url_for
from Model.engagement import Engagement
from Model.base import db
engagements = Blueprint('engagement', __name__)

@engagements.route('', methods=['GET'])
def list():
    objects = Engagement.query.all()

    engagementList = []

    for o in objects:
        engagementList.append({
                'id': o.engagement_id,
                'name': o.name,
                'budgeted_hours': o.budgeted_hours,
                'expect_hours': o.expect_hours,
                'actual_hours': o.actual_hours,
                'start_date': o.start_date if o.start_date else None,
                'finish_date': o.finish_date if o.finish_date else None,
                'last_entry_date': o.last_entry_date if o.last_entry_date else None,
                'hours_balance': o.hours_balance,
                'inactive_days': o.inactive_days if o.inactive_days else None
        })
    response = jsonify(engagementList)
    
    return response

@engagements.route('/<string:engagement_id>', methods=['GET'])
def engagement(engagement_id):

    e = Engagement.query.get_or_404(engagement_id)
    
    response =  jsonify({
        'id': e.engagement_id,
        'name': e.name,
        'budgeted_hours': e.budgeted_hours,
        'expect_hours': e.expect_hours,
        'actual_hours': e.actual_hours,
        'start_date': e.start_date if e.start_date else None,
        'finish_date': e.finish_date if e.finish_date else None,
        'last_entry_date': e.last_entry_date if e.last_entry_date else None,
        'hours_balance': e.hours_balance,
        'inactive_days': e.inactive_days if e.inactive_days else None
    })

    return response

