from flask import make_response,  jsonify
from flask_restful import Resource
from models import Person


class PersonResource(Resource):

    def get(self, cpf):
        person = Person.query.filter_by(cpf=cpf).first_or_404()
        return make_response(jsonify(person.serialize), 200)
