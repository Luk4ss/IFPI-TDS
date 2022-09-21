'''1) Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
a) Mostre a quantidade de números pares;
b) Grave uma lista somente com os números pares e mostre a lista;
c) Mostre a quantidade de números ímpares;
d) Grave uma lista somente com os números ímpares e mostre a lista. '''

from random import *

def seed_lista(lista):
    for i in range(100):
        random_number = randint(1, 99999)
        lista.append(random_number)


def seed_numeros_pares():
    pares = []
    contador = 0
    while contador < 100:      
        random_number = randint(1, 99999)    
        if random_number % 2 == 0:
            pares.append(random_number)
            contador += 1
    return pares
  

def seed_numeros_impares():
    impares = []
    contador = 0
    while contador < 100:      
        random_number = randint(1, 99999)    
        if random_number % 2 != 0:
            impares.append(random_number)
            contador += 1
    return impares


def conta_pares(lista):
    contador = 0
    for num in lista:
        if num % 2 == 0:
            contador += 1
    return contador


def conta_impares(lista):
    contador = 0
    for num in lista:
        if num % 2 != 0:
            contador += 1
    return contador


def main():
    minha_lista = []
    seed_lista(minha_lista)
    qtd_pares = conta_pares(minha_lista)
    qtd_impares = conta_impares(minha_lista)
    lista_pares = seed_numeros_pares()
    lista_impares = seed_numeros_impares()
    print(f'Quantidade de números pares na lista: {qtd_pares}')
    print(f'Quantidade de números ímpares na lista: {qtd_impares}')
    print('-----------------------------------')
    print(' ######   MINHA LISTA    ######')
    for num in minha_lista:
        print(f'{num}')
    print('-----------------------------------')
    print(' ######   LISTA DE PARES   ######')
    for num in lista_pares:
        print(f'{num}')
    print('-----------------------------------')
    print(' ######   LISTA DE ÍMPARES    ######')
    for num in lista_impares:
        print(f'{num}')
    print('-----------------------------------')
    


main()
