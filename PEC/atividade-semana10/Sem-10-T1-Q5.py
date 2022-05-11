
salario = float(input())

taxa_salario = 0.05

divida = float(input())

taxa_divida = 0.15

mes = 10

ano = 2016


while divida < salario:
    divida += divida * taxa_divida
    mes += 1
    if mes > 12:
        ano += 1
        mes = 1
    elif mes == 3:
        salario += salario * taxa_salario

print(f'{mes}/{ano}')
