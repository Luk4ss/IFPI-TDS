#coding: latin-1

"""9. Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e retorna a soma de todos os números inteiros contidos
no intervalo [n1,n2]. Use esta função em um programa que lê n1 e n2 do usuário e imprime a soma."""


def soma_intervalo(n1, n2):
    s = 0
    if n2 < 0:
        n2 -= 1
    else:
        n2 += 1
    for num in range(n1, n2):
        s += num
    return s


def main():
    while True:
        try:
            num1 = int(input('Digite o primeiro número do intervalo: '))
            num2 = int(input('Digite o segundo número do intervalo: '))
            if num2 < num1:
                aux = num2
                num2 = num1
                num1 = aux
            print(f'A soma dos numeros inteiros contigos no intervalo [{num1},{num2}] é igual a : {soma_intervalo(num1, num2)}')
            break
        except:
            print("!!! Dado inválido !!! Por favor, digite um número inteiro...")

if __name__ == '__main__':
    main()
