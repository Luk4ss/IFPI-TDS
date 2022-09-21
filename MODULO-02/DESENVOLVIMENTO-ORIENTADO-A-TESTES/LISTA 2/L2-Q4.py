'''4) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
a) O maior elemento da lista e em que posição esse elemento se encontra;
b) O menor elemento da lista e em que posição esse elemento se encontra.'''

from random import *

def seed_lista(lista):
   for i in range(15):
       lista.append(randint(-999, 999))


def procura_maior(lista):
    maior = lista[0]
    pos = 0
    for i in range(len(lista)):
        if lista[i] >= maior:
           maior = lista[i]
           pos = i
    return maior,pos    


def procura_menor(lista):
    menor = lista[0]
    pos = 0
    for i in range(len(lista)):
        if lista[i] <= menor:
           menor = lista[i]
           pos = i
    return menor,pos  



def main():
   l1 = []
   seed_lista(l1)
   print(l1)
   print("-----------------------------------")
   print("O maior elemento e sua posição")
   print(procura_maior(l1))
   print("------------------------------------")
   print("O menor elemento e sua posição")
   print(procura_menor(l1))


main()
