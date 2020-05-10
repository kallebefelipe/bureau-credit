from models import Person, LastBuyCard, Transaction
from .enums import persons


def initialize():
    Person.objects.delete()

    for person_info in persons:
        last_buy = LastBuyCard(
            data=person_info['ultima_compra_cartao']['data'],
            valor=person_info['ultima_compra_cartao']['valor']
        )

        list_transaction = []
        for mov in person_info['movimentacoes']:
            transaction = Transaction(
                tipo=mov.get('tipo'),
                valor=mov.get('valor')
            )
            list_transaction.append(transaction)

        person = Person(
            cpf=person_info.get('cpf'),
            data_consulta=person_info.get('data_consulta'),
            ultima_compra_cartao=last_buy,
            movimentacao=list_transaction
        )
        person.save()
