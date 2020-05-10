from db.db import db

class LastBuyCard(db.EmbeddedDocument):
    valor = db.IntField(required=True)
    data = db.DateTimeField(required=False)

class Transaction(db.EmbeddedDocument):
    valor = db.IntField(required=True)
    tipo = db.StringField(required=False)


class Person(db.Document):
    cpf = db.StringField(required=True)
    data_consulta = db.DateTimeField(required=False)
    ultima_compra_cartao = db.EmbeddedDocumentField('LastBuyCard')
    movimentacao = db.EmbeddedDocumentListField('Transaction')

    @property
    def serialize(self):
        return {
            'cpf': self.cpf,
            'data': self.data_consulta,
            'ultima_compra_cartao': {
                'data': self.ultima_compra_cartao.data,
                'valor': self.ultima_compra_cartao.valor
            },
            'movimentacoes': [{
                'tipo': moviment.tipo,
                'valor': moviment.valor
            } for moviment in self.movimentacao]
        }
