# LISTA 1 - QUESTÃO 3
"""
3 - Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma função chamada celsius para calcular e retornar
o valor correspondente em graus Celsius.
Fórmula: C = ((F-32)/9)*5
"""

def celsius(fahrenheit):
    return ((fahrenheit - 32)/9) * 5


while True:
    try:
        temperatura = float(input("Insira a temperatura em Fahrenheit: "))
        break
    except:
        print('Dado inválido! Por favor, digite novamente.')

print(f'A temperatura inserida equivale a: {celsius(temperatura):.2f} graus Celsius')
