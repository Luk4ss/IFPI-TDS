# LISTA 1 - QUESTÃO 5

"""
5 - Faça um programa que leia a altura e o sexo (codificado da seguinte forma: 1:feminino 2:masculino) de uma pessoa.
Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e que calcule e retorne
seu peso ideal, utilizando as seguintes fórmulas:
- para homens : (72.7 * h) – 58
- para mulheres : (62.1 * h) – 44.7
Observação: Altura = h (na fórmula acima).
"""

def peso_ideal(sexo, h):
    if sexo == 2:
        return (72.7 * h) - 58
    if sexo == 1:
        return (62.1 * h) - 44.7


def main():
    while True:
        try:
            print('''Digite o seu sexo:
            1 - Feminino
            2 - Masculino ''')
            opcao = int(input('Sua opção: '))
            while opcao not in [1, 2]:
                print('>> Opção inválida!! Digite a opção novamente.')
                opcao = int(input('Sua opção: '))
            altura = float(input('Digite a sua altura: '))
            break
        except:
            print(">>>>> Valor inválido. Por favor, Digite novamente\n")

    print(f'Seu peso ideal é: {peso_ideal(opcao, altura):.2f} kg')


if __name__ == '__main__':
    main()
