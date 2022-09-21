#coding: latin-1

"""7. Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial, sabemos que N! depende de (N-1)!; este por
sua vez depende de (N-2)!; e, assim por diante, até que N seja 1, quando então tem-se que fatorial de 1 é igual a 1 mesmo. Utilize
uma função que recebe como parâmetro de entrada o número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste
número, também do tipo inteiro. """


def fatorial(numero):
    acc = 1
    for i in range(numero, 1, -1):
        acc *= i
    return acc

def main():
    while True:
        try:
            n = int(input('Digite um número positivo: '))
            while n < 0:
                n = int(input('Número inválido. Por favor, digite novamente: '))
            print(f'O fatorial de {n} é: {fatorial(n)}')
            break
        except:
            print('!!! Dado Inválido !!! Por favor, digite um número válido.')


if __name__ == '__main__':
    main()
