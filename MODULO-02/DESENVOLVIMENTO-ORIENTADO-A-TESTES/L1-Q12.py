#coding: latin-1

"""12 - Escreva uma fun��o que recebe, por par�metro, um valor inteiro e positivo e retorna o somat�rio desse valor."""

def somatorio(n):
    # F�rmula da soma de uma PA
    return ((1 + n)*n) // 2

#region MAIN
def main():
    while True:
        try:
            numero = int(input('Digite um numero inteiro positivo: '))
            while numero <= 0:
                numero = int(input('N�mero inv�lido! Digite um n�mero positivo: '))
            print(f'O somat�rio de 1 at� {numero} � igual a : {somatorio(numero)}')
            break
        except:
            print('!!! Dado inv�lido !!! Digte um n�mero positivo!')

#endregion MAIN

if __name__ == '__main__':
    main()

    