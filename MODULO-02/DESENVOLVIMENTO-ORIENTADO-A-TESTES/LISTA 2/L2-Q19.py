''' 19) Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos
cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos
de S. Escrever a lista X. '''

from random import *

def criar_lista_com_n_elementos(qtd):
    ls = []
    for i in range(qtd):
        ls.append(randint(-999,999))
    return ls


def main():
    R = criar_lista_com_n_elementos(5)
    S = criar_lista_com_n_elementos(10)
    X = []
    for elemento in R:
        X.append(elemento)
    for elemento in S:
        X.append(elemento)        
    print("======================== LISTA R ===========================")
    print(R)
    print("\n======================== LISTA S ===========================")
    print(S)
    print("\n============================================ LISTA X ====================================================")
    print(X)


main()
