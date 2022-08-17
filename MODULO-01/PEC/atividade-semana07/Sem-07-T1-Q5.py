
def imc(peso, altura):
    IMC = int(peso // (altura ** 2))

    if IMC < 18.5:
        return f'{IMC}\nAbaixo do peso'
    elif IMC < 25.0:
        return f'{IMC}\nPeso normal'
    elif IMC < 30.0:
        return f'{IMC}\nSobrepeso'
    elif IMC < 35.0:
        return f'{IMC}\nObeso leve'
    elif IMC < 40.0:
        return f'{IMC}\nObeso moderado'
    elif IMC >= 40.0:
        return f'{IMC}\nObeso mórbido'


def main():
    peso = float(input())
    altura = float(input())
    print(imc(peso, altura))


if __name__ == '__main__':
    main()
