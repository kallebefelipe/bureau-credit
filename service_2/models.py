from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db.db import db
from utils.calc_score import calc_score

class Person(db.Model):
    cpf = db.Column(
        db.String(100), primary_key=True, unique=True, nullable=False)
    nome = db.Column(db.String(100), unique=False, nullable=False)
    endereco = db.relationship(
        'Address', uselist=False, backref='person')
    fonte_renda = db.relationship(
        'Income', backref='person')
    lista_bens = db.relationship(
        'Patrimony', backref='person')

    @property
    def score(self):
        return calc_score(self.fonte_renda, self.lista_bens)

    @property
    def serialize(self):
        return {
            'cpf': self.cpf,
            'nome': self.nome,
            'score': self.score,
            'endereco': {
                'rua': self.endereco.rua,
                'numero': self.endereco.numero,
                'cidade': self.endereco.cidade,
                'estado': self.endereco.estado
            },
            'fonte_renda': [{
                'tipo': divida.tipo,
                'valor': divida.valor
            } for divida in self.fonte_renda],
            'lista_bens': [{
                'tipo': patrimonio.tipo,
                'valor': patrimonio.valor
            } for patrimonio in self.lista_bens]
        }


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rua = db.Column(db.String(100), unique=True, nullable=True)
    numero = db.Column(db.Integer, unique=False, nullable=True)
    cidade = db.Column(db.String(100), unique=False, nullable=True)
    estado = db.Column(db.String(100), unique=False, nullable=True)
    person_id = db.Column(
        db.Integer, db.ForeignKey('person.cpf'), nullable=False)


class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100), unique=False, nullable=True)
    valor = db.Column(db.Integer, unique=False, nullable=True)
    person_id = db.Column(
        db.Integer, db.ForeignKey('person.cpf'), nullable=False)


class Patrimony(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100), unique=False, nullable=True)
    valor = db.Column(db.Integer, unique=False, nullable=True)
    person_id = db.Column(
        db.Integer, db.ForeignKey('person.cpf'), nullable=False)
