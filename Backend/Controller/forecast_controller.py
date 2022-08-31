from flask import jsonify, request, Blueprint, Response, render_template, redirect, url_for
# from Model.member import Member
# from Model.engagement import Engagement
# from Model.group_member import GroupMember

forecast = Blueprint('forecast', __name__)

@forecast.route('/forecast hours', methods=['POST', 'GET'])
def forecast_hours():

    if request.method == 'POST':
        data = request.form


    if request.method == 'GET':


        
