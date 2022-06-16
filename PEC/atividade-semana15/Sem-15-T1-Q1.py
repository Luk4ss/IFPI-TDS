def maior(n1, n2):
    return n1 if n1 > n2 else n2


def menor(n1, n2):
    return n2 if n1 > n2 else n1


def position(matriz, major, minor):
    pos_i_maior = 0
    pos_j_maior = 0
    pos_i_menor = 0
    pos_j_menor = 0

    for line in matriz:
        for number in line:
            if number == major:
                pos_i_maior = matriz.index(line)
                pos_j_maior = line.index(number)
            if number == minor:
                pos_i_menor = matriz.index(line)
                pos_j_menor = line.index(number)

    pos_maior = pos_i_maior, pos_j_maior
    pos_menor = pos_i_menor, pos_j_menor

    return pos_maior, pos_menor


matriz_A = []

n = int(input())

count = 0

while count < n:
    lista = []
    for i in range(0, n):
        lista.append(int(input()))
    matriz_A.append(lista)
    count += 1

maximo = -99999
minimo = 99999

for row in matriz_A:
    maximo = maior(maximo, max(row))
    minimo = menor(minimo, min(row))

t1, t2 = position(matriz_A, maximo, minimo)

print(t1)
print(t2)
