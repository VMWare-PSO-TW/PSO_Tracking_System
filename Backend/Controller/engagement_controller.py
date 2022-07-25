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
                'expect': o.expect_hours,
                'actual': o.actual_hours,
                'internal': o.internal_hours if o.internal_hours else None,
                'subb': o.subb_hours if o.subb_hours else None
        })

    return jsonify(engagementList)

@engagements.route('/<string:engagement_id>', methods=['GET'])
def engagement(engagement_id):

    e = Engagement.query.get_or_404(engagement_id)
    
    return jsonify({
        'id': e.engagement_id,
        'name': e.name,
        'expect': e.expect_hours,
        'actual': e.actual_hours,
        'internal': e.internal_hours if e.internal_hours else None,
        'subb': e.subb_hours if e.subb_hours else None
    })

