"""
    Áries	21/03 a 19/04
    Touro	20/04 a 20/05
    Gêmeos	21/05 a 21/06
    Câncer	22/06 a 22/07
    Leão	23/07 a 22/08
    Virgem	23/08 a 22/09
    Libra	23/09 a 22/10
    Escorpião	23/10 a 21/11
    Sagitário	22/11 a 21/12
    Capricórnio	22/12 a 19/01
    Aquário	20/01 a 18/02
    Peixes	19/02 a 20/03
"""

dia_nascimento = int(input())
mes_nascimento = int(input())


def signo(dia, mes):
    if mes == 1:
        if 1 <= dia <= 19:
            return 'Capricórnio'
        else:
            return 'Aquário'
    elif mes == 2:
        if 1 <= dia <= 18:
            return 'Aquário'
        else:
            return 'Peixes'
    elif mes == 3:
        if 1 <= dia <= 20:
            return 'Peixes'
        else:
            return 'Áries'
    elif mes == 4:
        if 1 <= dia <= 19:
            return 'Áries'
        else:
            return 'Touro'
    elif mes == 5:
        if 1 <= dia <= 20:
            return 'Touro'
        else:
            return 'Gêmeos'
    elif mes == 6:
        if 1 <= dia <= 21:
            return 'Gêmeos'
        else:
            return 'Câncer'
    elif mes == 7:
        if 1 <= dia <= 22:
            return 'Câncer'
        else:
            return 'Leão'
    elif mes == 8:
        if 1 <= dia <= 22:
            return 'Leão'
        else:
            return 'Virgem'
    elif mes == 9:
        if 1 <= dia <= 22:
            return 'Virgem'
        else:
            return 'Libra'
    elif mes == 10:
        if 1 <= dia <= 22:
            return 'Libra'
        else:
            return 'Escorpião'
    elif mes == 11:
        if 1 <= dia <= 21:
            return 'Escorpião'
        else:
            return 'Sagitário'
    elif mes == 12:
        if 1 <= dia <= 21:
            return 'Sagitário'
        else:
            return 'Capricórnio'


print(f'{signo(dia_nascimento, mes_nascimento)}')
