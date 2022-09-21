"""1 - Faça uma função que recebe um número inteiro por parâmetro e retorna verdadeiro se ele for par e
falso se for ímpar."""


def eh_par(n):
    return n % 2 == 0


def main():
    print(' ### PROGRAMA QUE VERIFICA SE O NÚMERO DIGITADO É PAR ###')
    while True:
        try:
            numero = int(input('Digite um número inteiro: '))
            print(f'>> {numero} é par? {eh_par(numero)}')
            break
        except:
            print(' >>>>>> Dado inválido. Por favor, digite um número inteiro.')


if __name__ == '__main__':
    main()
