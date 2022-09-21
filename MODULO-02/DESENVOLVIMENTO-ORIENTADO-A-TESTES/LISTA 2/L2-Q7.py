'''7) Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um
outro valor dado pertence ou não à lista.'''

from random import *

def seed_lista(ls):
    for i in range(10):
        random_number = randint(-999, 999)
        ls.append(random_number)


def procura_numero(number, ls):
    for n in ls:
        if number == n:
           return True
    return False


def main():
    lista = []
    seed_lista(lista)
    while True:
        try:
            dado = int(input('Digite um número inteiro: '))
            if procura_numero(dado, lista):
                print("O número digitado está na lista")
            else:
                print("O número digitado não pertence à lista...")

            print("================== LISTA =====================")
            print(lista)
            break
        except:
            print('\nDado inválido. Por favor, digite um número...\n')  

    
main()
