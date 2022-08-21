"""
6 - Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento
que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
- Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
- Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
- Se o número de lados for igual a 5, escrever PENTÁGONO.
Observação: Considere que o usuário só informará os valores 3, 4 ou 5.
"""


def poligono(n_lados, medida):
    # Como é um procedimento, a função não irá retornar nada. Somente irá imprimir uma mensagem na tela.
    if n_lados == 3:
        perimetro_triangulo = 3*medida
        print(f'TRIÂNGULO. Seu perímetro é igual a: {perimetro_triangulo:.2f} cm')
    elif n_lados == 4:
        area_quadrado = medida**2
        print(f'QUADRADO. Seu área é igual a: {area_quadrado:.2f} cm²')
    elif n_lados == 5:
        print('PENTÁGONO')


def main():
    while True:
        try:
            print('''INFORME O NÚMERO DE LADOS DO POLÍGONO. DIGITE:
            3 - TRIÂNGULO
            4 - QUADRADO
            5 - PENTÁGONO''')
            lados = int(input('Sua opção: '))
            while lados not in [3, 4, 5]:
                lados = int(input('Opção inválida! Digite novamente: '))
            medida_lado = float(input('Digite a medida do lado desse polígono: '))
            while medida_lado <= 0:
                medida_lado = float(input('Medida inválida! Digite novamente: '))
            poligono(lados, medida_lado)
            break
        except ValueError:
            print('!!!!! DADO INVÁLIDO !!!!! POR FAVOR, DIGITE UM DADO VÁLIDO...')


if __name__ == '__main__':
    main()
