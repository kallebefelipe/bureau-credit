from models import Person, Address, Income, Patrimony
from .enums import persons
from db.db import db



def initialize():
    db.drop_all()
    db.metadata.create_all(
        db.engine,
        tables=[
            Person.__table__,
            Address.__table__,
            Income.__table__,
            Patrimony.__table__
        ]
    )

    list_persons = []
    list_incomes = []
    list_address = []
    list_patrimony = []
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

        for income_info in person_info.get('fonte_renda'):
            income = Income(
                tipo=income_info.get('tipo'),
                valor=income_info.get('valor'),
                person_id=person_info.get('cpf')
            )
            list_incomes.append(income)

        for patrimony_info in person_info.get('lista_bens'):
            patrimony = Patrimony(
                tipo=patrimony_info.get('tipo'),
                valor=patrimony_info.get('valor'),
                person_id=person_info.get('cpf')
            )
            list_patrimony.append(patrimony)
    db.session.add_all(list_persons)
    db.session.add_all(list_incomes)
    db.session.add_all(list_address)
    db.session.add_all(list_patrimony)
    db.session.commit()
