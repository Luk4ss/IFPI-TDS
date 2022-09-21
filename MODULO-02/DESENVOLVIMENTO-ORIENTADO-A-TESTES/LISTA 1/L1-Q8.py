# LISTA 1 - QUESTÃO 8
"""
8 - Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a
'S' ou 'N'. Se o caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'.
 Use esta função em um programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela.
 O programa deve ficar lendo os números até o usuário responder 'N' à pergunta se ele deseja continuar ou não.
"""
def ler_caractere(c):
    while True:
        if c in ['S', 's', 'N', 'n']:
            return c
        c = input('Caractere inválido! Digite novamente: ')


while True:
    try:
        numero = float(input('Digite um Número: '))
        print(f'O cubo desse número é: {numero ** 3: .2f}')
        opt = input('Deseja continuar? ')
        res = ler_caractere(opt)
        print(f'Caractere digitado: {res}')
        if res in ['N', 'n']:
            break
    except:
        print('Dado inválido! Por favor digite novamente...')
