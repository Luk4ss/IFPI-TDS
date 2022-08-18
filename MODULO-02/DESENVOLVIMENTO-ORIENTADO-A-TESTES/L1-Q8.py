# LISTA 1 - QUESTÃO 8

def ler_caractere(c):
    if c in ['S', 's']:
        return c
    if c in ['N', 'n']:
        return c
    else:
        return ' !!!! Caractere inválido! Digite novamente!!!!'


while True:
    try:
        numero = float(input('Digite um Número: '))
        print(f'O cubo desse número é: {numero ** 3: .2f}')
        while True:
            opt = input('Deseja continuar? ')
            res = ler_caractere(opt)
            print(f'Caractere digitado: {res}')
            if res in ['N', 'S', 'n', 's']:
                break
        if res in ['N', 'n']:
            break
    except:
        print('Dado inválido! Por favor digite novamente...')
