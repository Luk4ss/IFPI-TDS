#coding: latin-1

"""11. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor."""

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
            numero = int(input('Digite um número inteiro positivo: '))
            while numero <= 0:
                numero = int(input('Número inválido. Por favor, digite um número positivo: '))
            print(f'A quantidade de divisores que o número {numero} possui é: {quantidade_divisores(numero)} ')
            break
        except:
            print('!!! Dado inválido !!! Digite um número inteiro positivo!')

#endregion MAIN

if __name__ == '__main__':
    main()
