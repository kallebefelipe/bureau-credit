import os

import flask
from flask_restful import Api
from mongoengine import connect
from mongoengine.connection import disconnect

from api import PersonScoreResource
from db.db import db
from scripts.initialize_db import initialize

mongo_url = os.getenv('MONGO_URL')

app = flask.Flask(__name__)
app.config['MONGODB_DB'] = 'basec'
app.config['MONGODB_HOST'] = mongo_url
connect(
    'basec',
    host=mongo_url,
    port=27017
)

resource_api = Api(app)
resource_api.add_resource(PersonScoreResource, '/evento/<string:cpf>')

def init():
    disconnect()
    db.init_app(app)
    with app.app_context():
        initialize()
    app.run(host='0.0.0.0', port=5002, debug=True)

init()
