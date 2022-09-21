# LISTA 1 - QUESTÃO 15

"""
15 - Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3)
"""

def calcula_expressao(n):
    s = 0
    for i in range(1, n + 1):
        s += (i ** 2 + 1) / (i + 3)
    return s


while True:
    try:

        N = int(input('Digite um número inteiro e positivo: '))
        while N <= 0:
            print('>> Número inválido! Por favor, digite um número positivo.')
            N = int(input('Digite um número inteiro e positivo: '))
        print(f'O resultado da expressão é: {calcula_expressao(N):.2f}')
        break
    except:
        print("Dado inválido! Por favor, Digite novamente...\n")
