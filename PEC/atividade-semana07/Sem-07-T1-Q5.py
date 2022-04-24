
def imc(peso, altura):
    return peso / (altura ** 2)


def main():
    peso = float(input())
    altura = float(input())

    IMC = imc(peso, altura)

    if IMC < 18.5:
        print('Abaixo do peso')
    elif IMC < 25.0:
        print('Peso normal')
    elif IMC < 30.0:
        print('Sobrepeso')
    elif IMC < 35.0:
        print('Obeso leve')
    elif IMC < 40.0:
        print('Obeso moderado')
    elif IMC >= 40.0:
        print('Abaixo do peso')


if __name__ == '__main__':
    main()
