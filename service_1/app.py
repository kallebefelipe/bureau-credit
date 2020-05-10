import os

import flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from api import PersonResource
from db.db import db
from scripts.initialize_db import initialize

database_uri = os.getenv('DATABASE_URI')

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

resource_api = Api(app)
resource_api.add_resource(PersonResource, '/pessoa/<string:cpf>')

def init():
    db.init_app(app)
    with app.app_context():
        initialize()
    app.run(host='0.0.0.0', debug=True)

init()
