#coding: latin-1

"""9. Escreva uma fun��o que recebe 2 n�meros inteiros n1 e n2 como entrada e retorna a soma de todos os n�meros inteiros contidos
no intervalo [n1,n2]. Use esta fun��o em um programa que l� n1 e n2 do usu�rio e imprime a soma."""


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
            num1 = int(input('Digite o primeiro n�mero do intervalo: '))
            num2 = int(input('Digite o segundo n�mero do intervalo: '))
            if num2 < num1:
                aux = num2
                num2 = num1
                num1 = aux
            print(f'A soma dos numeros inteiros contigos no intervalo [{num1},{num2}] � igual a : {soma_intervalo(num1, num2)}')
            break
        except:
            print("!!! Dado inv�lido !!! Por favor, digite um n�mero inteiro...")

if __name__ == '__main__':
    main()
