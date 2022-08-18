# LISTA 1 - QUESTÃO 14


def cacula_expressao(n):
    s = 0
    for i in range(1, n + 1):
        s += 1/fatorial(i)
    return s


def fatorial(k):
    acc = 1
    for i in range(k, 1, -1):
        acc *= i
    return acc


while True:
    try:
        numero = int(input('Digite um número inteiro positivo: '))
        while numero <= 0:
            print('>>>>Número inválido... por favor, digite um número positivo e maior que Zero.\n')
            numero = int(input('Digite um número inteiro positivo: '))
        print(f'O resultado da expressão é: {cacula_expressao(numero):.3f}')
        break
    except:
        print('Dado inválido! Por favor, digite novamente')
