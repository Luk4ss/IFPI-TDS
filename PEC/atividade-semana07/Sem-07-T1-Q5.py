
def imc(peso, altura):
    IMC = peso / (altura ** 2)

    if IMC < 18.5:
        return 'Abaixo do peso'
    elif IMC < 25.0:
        return 'Peso normal'
    elif IMC < 30.0:
        return 'Sobrepeso'
    elif IMC < 35.0:
        return 'Obeso leve'
    elif IMC < 40.0:
        return 'Obeso moderado'
    elif IMC >= 40.0:
        return 'Obeso mórbido'


def main():
    peso = float(input())
    altura = float(input())
    print(imc(peso, altura))


if __name__ == '__main__':
    main()
