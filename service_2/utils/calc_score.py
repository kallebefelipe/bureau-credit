

def calc_score(fonte_renda, lista_bens):
    sum_income = 0
    sum_patrimony = 0

    for income in fonte_renda:
        sum_income += income.valor

    for patrimony in lista_bens:
        sum_patrimony += patrimony.valor

    if sum_income == 0:
        return 0
    else:
        return int(sum_patrimony/sum_income)
