'''9) Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela
uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa. '''

from random import *

def reverte_lista(ls):
    last_index = len(ls) - 1
    rev = [0] * len(ls)
    index = 0
    for i in range(last_index, -1 , -1):
        rev[index] = ls[i]
        index += 1 
    return rev


def seed_lista(ls):
    for i in range(5):
        ls.append(randint(-99, 99))
    

def main():
    lista = []
    seed_lista(lista)
    lista_reversa = reverte_lista(lista)
    print("=============== LISTA =================")
    print(lista)
    print("=========== LISTA REVERSA =============")
    print(lista_reversa)
    print("====== LISTA REVERSA COM REVERSED =====")
    print(list(reversed(lista)))
    

main()
