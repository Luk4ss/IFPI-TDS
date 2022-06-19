def maior(n1, n2):
    return n1 if n1 > n2 else n2


def menor(n1, n2):
    return n2 if n1 > n2 else n1


def position_maior(matriz, major):
    pos_maior = 0
    for line in matriz:
        for number in line:
            if number == major:
                pos_maior = matriz.index(line), line.index(number)
                return pos_maior

    return pos_maior


def position_menor(matriz, minor):
    pos_menor = 0
    for line in matriz:
        for number in line:
            if number == minor:
                pos_menor = matriz.index(line), line.index(number)
                return pos_menor
    return pos_menor


matriz_A = []

n = int(input())
m = int(input())

count = 0


while count < n:
    lista = []
    for i in range(0, m):
        lista.append(int(input()))
    matriz_A.append(lista)
    count += 1


maximo = -99999
minimo = 99999

for row in matriz_A:
    maximo = maior(maximo, max(row))
    minimo = menor(minimo, min(row))

soma_ultima_coluna = 0
medias_linha = 0

for row in matriz_A:
    for i in range(0, len(row)):
        if i == (len(row) - 1):
            soma_ultima_coluna += row[i]
    medias_linha += sum(row) / len(row)

t1 = position_maior(matriz_A, maximo)
t2 = position_menor(matriz_A, minimo)

soma_primeira_linha = sum(matriz_A[0])
maior_elemento = matriz_A[t1[0]][t1[1]]
menor_elemento = matriz_A[t2[0]][t2[1]]

media_total = medias_linha/(len(matriz_A))

tupla_final = (soma_primeira_linha, soma_ultima_coluna, media_total.__round__(4), menor_elemento, maior_elemento)

print(tupla_final)
'''
print(f'Soma da primeira linha: {soma_primeira_linha}')
print(f'Soma da Última Coluna: {soma_ultima_coluna}')
print(f'Media: {media_total}')
print(f'Menor elemento: {menor_elemento}')
print(f'Maior elemento: {maior_elemento}')
'''
