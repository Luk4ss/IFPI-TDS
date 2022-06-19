matriz_A = []

n = 5
m = 7
ano = 2013
count = 0

while count < n:
    lista = []
    for i in range(m):
        if count == 0 and i == 0:
            lista.append('Fabricante/Ano')
        elif count == 0 and i == 1:
            lista.append(2013)
        elif count == 0 and i == 2:
            lista.append(2014)
        elif count == 0 and i == 3:
            lista.append(2015)
        elif count == 0 and i == 4:
            lista.append(2016)
        elif count == 0 and i == 5:
            lista.append(2017)
        elif count == 0 and i == 6:
            lista.append(2018)
        elif count == 1 and i == 0:
            lista.append('Fiat')
        elif count == 2 and i == 0:
            lista.append('Ford')
        elif count == 3 and i == 0:
            lista.append('GM')
        elif count == 4 and i == 0:
            lista.append('Wolkswagen')
        else:
            lista.append(int(input()))
    matriz_A.append(lista)
    count += 1


search = int(input())

maior_venda = 0

for i in range(1, 7):
    if matriz_A[0][i] == search:
        maior_venda = max(matriz_A[1][i], matriz_A[2][i], matriz_A[3][i], matriz_A[4][i])

total_vendas_por_ano = []
for i in range(1, 7):
    soma = 0
    for j in range(1, 5):
        if i == 1:
            soma += matriz_A[j][i]
        elif i == 2:
            soma += matriz_A[j][i]
        elif i == 3:
            soma += matriz_A[j][i]
        elif i == 4:
            soma += matriz_A[j][i]
        elif i == 5:
            soma += matriz_A[j][i]
        elif i == 6:
            soma += matriz_A[j][i]
    total_vendas_por_ano.append(soma)

maior_ano_de_vendas = max(total_vendas_por_ano)

ano_maior_venda = matriz_A[0][total_vendas_por_ano.index(maior_ano_de_vendas) + 1]


#  O denominador (7 - 1) é por causa do número de colunas - 7, para retirar os nomes Fiat,ford e etc.
media_fiat = sum(matriz_A[1][1::])/(7 - 1)
media_ford = sum(matriz_A[2][1::])/(7 - 1)
media_gm = sum(matriz_A[3][1::])/(7 - 1)
media_wolkswagen = sum(matriz_A[4][1::])/(7 - 1)

empresa = ''
year_maior = 0

for linha in range(5):
    for coluna in range(7):
        if matriz_A[linha][coluna] == maior_venda:
            empresa = matriz_A[linha][0]
            year_maior = matriz_A[0][coluna]


print(f'A fabricante que mais vendeu em {year_maior} foi a {empresa} com {maior_venda} mil unidades.')
print(f'O ano de maior volume geral de vendas foi {ano_maior_venda} com {maior_ano_de_vendas} mil unidades.')
print('A média anual de vendas de cada fabricante entre 2013 e 2018 foi:')
print('A Fiat vendeu em média', media_fiat.__round__(2), 'unidades por ano.')
print('A Ford vendeu em média', media_ford.__round__(2), 'unidades por ano.')
print('A GM vendeu em média', media_gm.__round__(2), 'unidades por ano.')
print('A Wolkswagen vendeu em média', media_wolkswagen.__round__(2), 'unidades por ano.')

# imprimir a Matriz de vendas
"""
for row in matriz_A:
    print(row)
"""



