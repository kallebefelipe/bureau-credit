from flask import make_response,  jsonify
from flask_restful import Resource
from models import Person


class PersonScoreResource(Resource):

    def get(self, cpf):
        person = Person.objects.get_or_404(cpf=cpf)
        return make_response(jsonify(person.serialize), 200)
