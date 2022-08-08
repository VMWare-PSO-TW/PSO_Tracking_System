from flask import Flask

import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

from Model.base import db
from Model.engagement import Engagement
from Model.phase import Phase
from Model.group_member import GroupMember
from Model.group import Group
from Model.member import Member

from Controller.engagement_controller import engagements
from Controller.phase_controller import phases

from flask_migrate import Migrate   #載入migrate擴充套件

from flask.blueprints import Blueprint

from settings import db_user, db_pass, db_host, db_name

from flask_cors import CORS

def create_app(config_name='development'):
    print('current envrionment: ', config_name)

    app = Flask(__name__)
    app.url_map.strict_slashes = False

    CORS(app)



    app.config['SECRET_KEY'] = '123456'

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    
    print('db name ', db_name)

    db.init_app(app)
    Migrate(app, db, compare_type=True)  #註冊migrate到flask
    print('======app=====')

    prefix_url = Blueprint('prefix_url', __name__)

    prefix_url.register_blueprint(engagements, url_prefix='/engagement')
    prefix_url.register_blueprint(phases, url_prefix='/phase')

    app.register_blueprint(prefix_url, url_prefix='/server/api/v1')
    

    return app

