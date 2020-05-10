import os

import flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from api import PersonScoreResource
from db.db import db
from scripts.initialize_db import initialize

database_uri = os.getenv('DATABASE_URI')

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

resource_api = Api(app)
resource_api.add_resource(PersonScoreResource, '/score/<string:cpf>')

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        initialize()
    app.run(host='0.0.0.0', port=5001, debug=True)
