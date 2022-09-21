'''2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade
de números negativos e a soma dos números positivos dessa lista.'''

from random import *

def seed_lista(lista):
    for num in range(10):
        random_number = uniform(-9999, 9999).__round__(2)
        lista.append(random_number)

  

def main():
    minha_lista = []
    seed_lista(minha_lista)
    contador_de_numeros_negativos = 0
    soma_numeros_positivos = 0
    for num in minha_lista:
        if num < 0:
            contador_de_numeros_negativos += 1
        else:
            soma_numeros_positivos += num

    print(' ---------- LISTA DE NÚMEROS --------')
    for num in minha_lista:
        print(f'{num}', end=' ')
    print('\n-------------------------------------')
    print(f'\nEssa lista possui {contador_de_numeros_negativos} números negativos.')
    print(f'A soma dos números positivos dessa lista é igual a: {soma_numeros_positivos:.2f}')


main()
