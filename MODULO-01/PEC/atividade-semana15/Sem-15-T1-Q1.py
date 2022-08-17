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

t1 = position_maior(matriz_A, maximo)
t2 = position_menor(matriz_A, minimo)

print(t1)
print(t2)
