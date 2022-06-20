def createSheet(matriz, m, n):
    count = 0
    while count < m:
        lista = []
        for i in range(n):
            if i == 0 and count == 0:
                lista.append('MESES')
            elif i == 1 and count == 0:
                lista.append('Filial 1')
            elif i == 2 and count == 0:
                lista.append('Filial 2')
            elif i == 3 and count == 0:
                lista.append('Filial 3')
            elif i == 4 and count == 0:
                lista.append('TOTAL')
            elif i == 0 and count == 1:
                lista.append('Janeiro')
            elif i == 0 and count == 2:
                lista.append('Fevereiro')
            elif i == 0 and count == 3:
                lista.append('Março')
            elif i == 0 and count == 4:
                lista.append('Abril')
            elif i == 0 and count == 5:
                lista.append('Maio')
            elif i == 0 and count == 6:
                lista.append('Junho')
            elif i == 0 and count == 7:
                lista.append('Julho')
            elif i == 0 and count == 8:
                lista.append('Agosto')
            elif i == 0 and count == 9:
                lista.append('Setembro')
            elif i == 0 and count == 10:
                lista.append('Outubro')
            elif i == 0 and count == 11:
                lista.append('Novembro')
            elif i == 0 and count == 12:
                lista.append('Dezembro')
            elif i == 0 and count == 13:
                lista.append('TOTAL')
            else:
                lista.append(0)
        matriz.append(lista)
        count += 1
    # Filial 1
    for i in range(1, 13):
        matriz[i][1] = int(input())

    # Filial 2
    for i in range(1, 13):
        matriz[i][2] = int(input())

    # Filial 3
    for i in range(1, 13):
        matriz[i][3] = int(input())


def totalFilial(matriz, filial):
    soma = 0
    for i in range(1, 13):
        soma += matriz[i][filial]
    matriz[13][filial] = soma


ano_2014 = []
ano_2015 = []
ano_2016 = []
ano_2017 = []

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro')

linhas = 14
colunas = 5

createSheet(ano_2014, linhas, colunas)
createSheet(ano_2015, linhas, colunas)
createSheet(ano_2016, linhas, colunas)
createSheet(ano_2017, linhas, colunas)

totalFilial(ano_2014, 1)
totalFilial(ano_2014, 2)
totalFilial(ano_2014, 3)

totalFilial(ano_2015, 1)
totalFilial(ano_2015, 2)
totalFilial(ano_2015, 3)

totalFilial(ano_2016, 1)
totalFilial(ano_2016, 2)
totalFilial(ano_2016, 3)

totalFilial(ano_2017, 1)
totalFilial(ano_2017, 2)
totalFilial(ano_2017, 3)

total_2014 = ano_2014[13][1] + ano_2014[13][2] + ano_2014[13][3]
total_2015 = ano_2015[13][1] + ano_2015[13][2] + ano_2015[13][3]
total_2016 = ano_2016[13][1] + ano_2016[13][2] + ano_2016[13][3]
total_2017 = ano_2017[13][1] + ano_2017[13][2] + ano_2017[13][3]

for i in range(1, 13):
    print(f'2014;{ano_2014[0][1]};{ano_2014[i][0]};{ano_2014[i][1]}')

print(f'TOTAL 2014 FILIAL 1;{ano_2014[13][1]}')

for i in range(1, 13):
    print(f'2014;{ano_2014[0][2]};{ano_2014[i][0]};{ano_2014[i][2]}')

print(f'TOTAL 2014 FILIAL 2;{ano_2014[13][2]}')

for i in range(1, 13):
    print(f'2014;{ano_2014[0][3]};{ano_2014[i][0]};{ano_2014[i][3]}')

print(f'TOTAL 2014 FILIAL 3;{ano_2014[13][3]}')
print(f'TOTAL 2014 TODAS FILIAIS;{total_2014}')

for i in range(1, 13):
    print(f'2015;{ano_2015[0][1]};{ano_2015[i][0]};{ano_2015[i][1]}')

print(f'TOTAL 2015 FILIAL 1;{ano_2015[13][1]}')

for i in range(1, 13):
    print(f'2015;{ano_2015[0][2]};{ano_2015[i][0]};{ano_2015[i][2]}')

print(f'TOTAL 2015 FILIAL 2;{ano_2015[13][2]}')

for i in range(1, 13):
    print(f'2015;{ano_2015[0][3]};{ano_2015[i][0]};{ano_2015[i][3]}')

print(f'TOTAL 2015 FILIAL 3;{ano_2015[13][3]}')
print(f'TOTAL 2015 TODAS FILIAIS;{total_2015}')


for i in range(1, 13):
    print(f'2016;{ano_2016[0][1]};{ano_2016[i][0]};{ano_2016[i][1]}')

print(f'TOTAL 2016 FILIAL 1;{ano_2016[13][1]}')

for i in range(1, 13):
    print(f'2016;{ano_2016[0][2]};{ano_2016[i][0]};{ano_2016[i][2]}')

print(f'TOTAL 2016 FILIAL 2;{ano_2016[13][2]}')

for i in range(1, 13):
    print(f'2016;{ano_2016[0][3]};{ano_2016[i][0]};{ano_2016[i][3]}')

print(f'TOTAL 2016 FILIAL 3;{ano_2016[13][3]}')
print(f'TOTAL 2016 TODAS FILIAIS;{total_2016}')

for i in range(1, 13):
    print(f'2017;{ano_2017[0][1]};{ano_2017[i][0]};{ano_2017[i][1]}')

print(f'TOTAL 2017 FILIAL 1;{ano_2017[13][1]}')

for i in range(1, 13):
    print(f'2017;{ano_2017[0][2]};{ano_2017[i][0]};{ano_2017[i][2]}')

print(f'TOTAL 2017 FILIAL 2;{ano_2017[13][2]}')

for i in range(1, 13):
    print(f'2017;{ano_2017[0][3]};{ano_2017[i][0]};{ano_2017[i][3]}')

print(f'TOTAL 2017 FILIAL 3;{ano_2017[13][3]}')
print(f'TOTAL 2017 TODAS FILIAIS;{total_2017}')

total = total_2014 + total_2015 + total_2016 + total_2017
print(f'TOTAL PERÍODO TODAS FILIAIS;{total}')
