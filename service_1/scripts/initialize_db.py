from models import Person, Address, Debt
from .enums import persons
from db.db import db



def initialize():
    db.drop_all()
    db.metadata.create_all(
        db.engine,
        tables=[
            Person.__table__,
            Address.__table__,
            Debt.__table__]
    )

    list_persons = []
    list_debts = []
    list_address = []
    for person_info in persons:
        person = Person(
            cpf=person_info.get('cpf'),
            nome=person_info.get('nome')
        )

        address = Address(
            rua=person_info['endereco']['rua'],
            numero=person_info['endereco']['numero'],
            cidade=person_info['endereco']['cidade'],
            estado=person_info['endereco']['estado'],
            person_id=person_info.get('cpf')
        )

        list_address.append(address)
        list_persons.append(person)

        for debt_info in person_info.get('lista_dividas'):
            debt = Debt(
                tipo=debt_info.get('tipo'),
                valor=debt_info.get('valor'),
                person_id=person_info.get('cpf')
            )
            list_debts.append(debt)
    db.session.add_all(list_persons)
    db.session.add_all(list_debts)
    db.session.add_all(list_address)
    db.session.commit()
