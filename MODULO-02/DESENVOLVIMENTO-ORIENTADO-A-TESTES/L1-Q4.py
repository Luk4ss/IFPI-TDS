"""
4 - Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que receba
as duas notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!”
somente se o aluno foi aprovado (considere 6.0 a média mínima para aprovação).
"""


def status_aluno(n1, n2):
    # Como é um procedimento, a função não irá retornar nada. Somente irá imprimir uma mensagem na tela.
    media = ((n1 + n2) / 2).__round__(1)
    print(f'A média das duas notas é igual a: {media}')
    if media >= 6:
        print('>>>> PARABÉNS! Você foi aprovado!')
    else:
        print('>>>> Você foi reprovado...')


def main():
    while True:
        try:
            nota1 = float(input('Digite a primeira nota do aluno: '))
            nota2 = float(input('Digite a segunda nota do aluno: '))
            while nota1 * nota2 < 0 or nota2 > 10 or nota1 > 10:
                print('Por favor, digite valores que pertencem ao intervalo de 0 a 10...')
                nota1 = float(input('Digite a primeira nota do aluno: '))
                nota2 = float(input('Digite a segunda nota do aluno: '))
            status_aluno(nota1, nota2)
            break

        except ValueError:
            print('!!! DADO INVÁLIDO !!!!Por favor, digite um dado válido...')


if __name__ == '__main__':
    main()
