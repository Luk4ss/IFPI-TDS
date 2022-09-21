''' 16) Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os
elementos de Y com índice par receberão os respectivos elementos de X divididos por 2; os
elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3.
Escrever as listas X e Y.'''

from random import *

def criar_lista():
    ls = []
    for i in range(10):
        ls.append(randint(-999,999))
    return ls


def main():
    X = criar_lista()
    tamnho_lista_X = len(X)
    Y = [0] * tamnho_lista_X
    for i in range(tamnho_lista_X):
        if i % 2 == 0:
            Y[i] = X[i] // 2
        else:
            Y[i] = X[i] * 3

    print("======================== LISTA X ========================")
    print(X)
    print("\n======================== LISTA Y =======================")
    print(Y)



main()
