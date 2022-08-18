# LISTA 1 - QUESTÃO 3


def celsius(fahrenheit):
    return ((fahrenheit - 32)/9) * 5


while True:
    try:
        temperatura = float(input("Insira a temperatura em Fahrenheit: "))
        break
    except:
        print('Dado inválido! Por favor, digite novamente.')

print(f'A temperatura inserida equivale a: {celsius(temperatura):.2f} graus Celsius')
