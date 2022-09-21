#coding: latin-1

def somatorio_fracoes(n):
    s = 0
    for i in range(1, n + 1):
        s += 1/i
    return s

#region MAIN
def main():
    while True:
        try:
            numero = int(input('Digite um número inteiro positivo: '))
            while numero <= 0:
                numero = int(input("Número inválido! Digite um número inteiro positivo! "))
            print(f'O somatório das frações até 1/{numero} é igual a: {somatorio_fracoes(numero):.2f}')
            break
        except:
            print('!! DADO INVÁLIDO !! Digite um número inteiro positivo!')

    

#endregion MAIN

if __name__ == '__main__':
    main()
