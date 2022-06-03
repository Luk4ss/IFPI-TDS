
def tamanho(lista):
    tam = 0
    for _ in lista:
        tam += 1
    return tam


def soma(lista):
    total = 0
    for elemento in lista:
        total += elemento
    return total


def inverter(lista):
    lista_reversed = []
    for elemento in lista:
        lista_reversed.insert(0, elemento)
    return lista_reversed


def minimo(lista):
    menor = 99999999
    for elemento in lista:
        if elemento < menor:
            menor = elemento

    return menor


def maximo(lista):
    maior = -99999999
    for elemento in lista:
        if elemento > maior:
            maior = elemento
    return maior


lis = []

while True:
    opt = int(input().strip())
    if opt == 0:
        break
    lis.append(opt)

if len(lis):
    print(lis)
    print(tamanho(lis))
    print(inverter(lis))
    print(minimo(lis))
    print(maximo(lis))
    print(soma(lis))

else:
    print(lis)
    print(tamanho(lis))
    print(inverter(lis))
    print(0)
    print(0)
    print(0)
