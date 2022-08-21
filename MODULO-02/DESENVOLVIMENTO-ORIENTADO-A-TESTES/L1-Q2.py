"""
2 - Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada área que calcula e retorna
a área do círculo e outra função chamada perímetro que calcula e retorna o perímetro do círculo.
"""

from math import pi


def area_circuferencia(r):
    # retorna a área da circunferência arredondadno para três casas decimais
    return (pi * (r ** 2)).__round__(3)


def perimetro_circunferencia(r):
    # retorna o perímetro da circunferência arredondadno para três casas decimais
    return (2 * pi * r).__round__(3)


def main():
    while True:
        try:
            raio = float(input('Digite o valor do raio da circuferência: '))
            while raio <= 0:
                raio = float(input('Valor inválido, por favor digite um número maior do que zero: '))
            area = area_circuferencia(raio)
            perimetro = perimetro_circunferencia(raio)
            print(f'>> A área da circunferência de raio {raio} cm é igual: {area} cm²')
            print(f'>> O perímetro da circunferência de raio {raio} cm é: {perimetro} cm²')
            break
        except ValueError:
            print('!!!!!!!! DADO INVÁLIDO. POR FAVOR, DIGITE UM NÚMERO VÁLIDO.')

if __name__ == '__main__':
    main()
