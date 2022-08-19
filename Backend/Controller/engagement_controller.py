from flask import jsonify, request, Blueprint, Response, render_template, redirect, url_for
from Model.engagement import Engagement
from Model.base import db


engagements = Blueprint('engagement', __name__)


@engagements.route('/', methods=['GET'])
def list():
    objects = Engagement.query.all()

    engagementList = []

    for o in objects:
        engagementList.append({
                'id': o.engagement_id,
                'name': o.name,
                'budgeted': o.budgeted_hours,
                'expect': o.expect_hours,
                'actual': o.actual_hours,
                'internal': o.internal_hours if o.internal_hours else None,
                'subb': o.subb_hours if o.subb_hours else None,
                'current_qtr_planned_hours': o.current_qtr_planned_hours if o.current_qtr_planned_hours else None,
                'forecast_hours_this_qtr': o.forecast_hours_this_qtr if o.forecast_hours_this_qtr else None,
                'start_date': o.start_date if o.start_date else None,
                'last_entry_date': o.last_entry_date if o.last_entry_date else None,
                'hours_balance': o.hours_balance,
                'inactive_days': o.inactive_days
        })

    return jsonify(engagementList)

@engagements.route('/<string:engagement_id>', methods=['GET'])
def engagement(engagement_id):

    e = Engagement.query.get_or_404(engagement_id)
    
    return jsonify({
        'id': e.engagement_id,
        'name': e.name,
        'budgeted': e.budgeted_hours,
        'expect': e.expect_hours,
        'actual': e.actual_hours,
        'internal': e.internal_hours if e.internal_hours else None,
        'subb': e.subb_hours if e.subb_hours else None,
        'current_qtr_planned_hours': e.current_qtr_planned_hours if e.current_qtr_planned_hours else None,
        'forecast_hours_this_qtr': e.forecast_hours_this_qtr if e.forecast_hours_this_qtr else None,
        'start_date': e.start_date if e.start_date else None,
        'last_entry_date': e.last_entry_date if e.last_entry_date else None,
        'hours_balance': e.hours_balance,
        'inactive_days': e.inactive_days
    })

