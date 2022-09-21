#coding: latin-1

"""11. Fa�a uma fun��o que recebe, por par�metro, um valor inteiro e positivo e retorna o n�mero de divisores desse valor."""

def quantidade_divisores(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

#region MAIN

def main():
    while True:
        try:
            numero = int(input('Digite um n�mero inteiro positivo: '))
            while numero <= 0:
                numero = int(input('N�mero inv�lido. Por favor, digite um n�mero positivo: '))
            print(f'A quantidade de divisores que o n�mero {numero} possui �: {quantidade_divisores(numero)} ')
            break
        except:
            print('!!! Dado inv�lido !!! Digite um n�mero inteiro positivo!')

#endregion MAIN

if __name__ == '__main__':
    main()
