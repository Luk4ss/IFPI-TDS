'''18) Ler uma lista X de 10 elementos. A seguir copiar todos os valores negativos da lista X para
uma lista R, sem deixar elementos vazios entre os valores copiados. Escrever as listas X e R.'''

from random import *

def criar_lista():
    ls = []
    for i in range(10):
        ls.append(randint(-999,999))
    return ls


def copia_valores_negativos(ls_numeros):
    lista_negativos = []
    for numero in ls_numeros:
        if numero < 0:
            lista_negativos.append(numero)
    return lista_negativos


def main():
    X = criar_lista()
    R = copia_valores_negativos(X)
    print("===================== LISTA X ==========================")
    print(X)
    if len(R) > 0:
        print("\n================== LISTA R =========================")
        print(R)
    else:
        print("\nA lista R está vazia pois não há valores negativos na lista X")


main()
