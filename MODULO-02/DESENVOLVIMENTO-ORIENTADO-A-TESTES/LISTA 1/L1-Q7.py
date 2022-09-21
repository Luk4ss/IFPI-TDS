#coding: latin-1

"""7. Fa�a um programa para calcular o Fatorial de um n�mero. Para o c�lculo do fatorial, sabemos que N! depende de (N-1)!; este por
sua vez depende de (N-2)!; e, assim por diante, at� que N seja 1, quando ent�o tem-se que fatorial de 1 � igual a 1 mesmo. Utilize
uma fun��o que recebe como par�metro de entrada o n�mero a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste
n�mero, tamb�m do tipo inteiro. """


def fatorial(numero):
    acc = 1
    for i in range(numero, 1, -1):
        acc *= i
    return acc

def main():
    while True:
        try:
            n = int(input('Digite um n�mero positivo: '))
            while n < 0:
                n = int(input('N�mero inv�lido. Por favor, digite novamente: '))
            print(f'O fatorial de {n} �: {fatorial(n)}')
            break
        except:
            print('!!! Dado Inv�lido !!! Por favor, digite um n�mero v�lido.')


if __name__ == '__main__':
    main()
