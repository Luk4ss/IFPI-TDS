"""10. Escreva um programa composto de uma função Max e o programa principal como segue:
O programa principal lê 4 séries de 4 números a, b. Para cada série lida imprime o maior dos quatro números usando a 
função Max."""

def max(a, b, c, d):
    maior = a
    if b >= maior:
        maior = b
    if c >= maior:
        maior = c
    if d >= maior:
        maior = d
    return maior

#region MAIN

def main():
    for i in range(1, 5):
        while True:
            print(f' >>> Série No#{i} <<<')
            try:
                n1 = int(input('Número 1: '))
                n2 = int(input('Número 2: '))
                n3 = int(input('Número 3: '))
                n4 = int(input('Número 4: '))
                break
            except:
                print('### Dado inválido! Por favor, digite novamente! ###\n')
        print(f'>>>> O maior número dessa série é: {max(n1, n2, n3, n4)}\n')

#endregion MAIN

if __name__ == '__main__':
    main()

