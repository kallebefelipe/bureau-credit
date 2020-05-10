from datetime import datetime

data_now = datetime.now()

persons = [
    {
        'cpf': '085.218.774-01',
        'data_consulta': data_now,
        'ultima_compra_cartao': {
            'data': data_now,
            'valor': 1200
        },
        'movimentacoes': [{
            'tipo': 'saque',
            'valor': 500
        },
        {
            'tipo': 'pagamento',
            'valor': 100
        },
        {
            'tipo': 'transferencia',
            'valor': 200
        }]
    },
    {
        'cpf': '085.218.774-02',
        'data_consulta': data_now,
        'ultima_compra_cartao': {
            'data': data_now,
            'valor': 400
        },
        'movimentacoes': [{
            'tipo': 'saque',
            'valor': 50
        },
        {
            'tipo': 'pagamento',
            'valor': 100
        },
        {
            'tipo': 'transferencia',
            'valor': 200
        },
        {
            'tipo': 'pagamento',
            'valor': 300
        },
        {
            'tipo': 'saque',
            'valor': 150
        }]
    },
    {
        'cpf': '085.218.774-03',
        'nome': 'Jose da Silva',
        'data_consulta': data_now,
        'ultima_compra_cartao': {
            'data': data_now,
            'valor': 2000
        },
        'movimentacoes': [{
            'tipo': 'saque',
            'valor': 600
        },
        {
            'tipo': 'pagamento',
            'valor': 50
        },
        {
            'tipo': 'pagamento',
            'valor': 200
        },
        {
            'tipo': 'transferencia',
            'valor': 300
        },
        {
            'tipo': 'transferencia',
            'valor': 300
        },
        {
            'tipo': 'saque',
            'valor': 900
        }]
    },
]
