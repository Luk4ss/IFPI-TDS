#coding: latin-1

"""12 - Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor."""

def somatorio(n):
    # Fórmula da soma de uma PA
    return ((1 + n)*n) // 2

#region MAIN
def main():
    while True:
        try:
            numero = int(input('Digite um numero inteiro positivo: '))
            while numero <= 0:
                numero = int(input('Número inválido! Digite um número positivo: '))
            print(f'O somatório de 1 até {numero} é igual a : {somatorio(numero)}')
            break
        except:
            print('!!! Dado inválido !!! Digte um número positivo!')

#endregion MAIN

if __name__ == '__main__':
    main()

    