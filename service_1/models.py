from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db.db import db

class Person(db.Model):
    cpf = db.Column(
        db.String(100), primary_key=True, unique=True, nullable=False)
    nome = db.Column(db.String(100), unique=False, nullable=False)
    endereco = db.relationship(
        'Address', uselist=False, backref='person')
    lista_dividas = db.relationship(
        'Debt', backref='person')

    @property
    def serialize(self):
        return {
            'cpf': self.cpf,
            'nome': self.nome,
            'endereco': {
                'rua': self.endereco.rua,
                'numero': self.endereco.numero,
                'cidade': self.endereco.cidade,
                'estado': self.endereco.estado
            },
            'lista_dividas': [{
                'tipo': divida.tipo,
                'valor': divida.valor
            } for divida in self.lista_dividas]
        }


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rua = db.Column(db.String(100), unique=True, nullable=True)
    numero = db.Column(db.Integer, unique=False, nullable=True)
    cidade = db.Column(db.String(100), unique=False, nullable=True)
    estado = db.Column(db.String(100), unique=False, nullable=True)
    person_id = db.Column(
        db.Integer, db.ForeignKey('person.cpf'), nullable=False)


class Debt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100), unique=False, nullable=True)
    valor = db.Column(db.Integer, unique=False, nullable=True)
    person_id = db.Column(
        db.Integer, db.ForeignKey('person.cpf'), nullable=False)
