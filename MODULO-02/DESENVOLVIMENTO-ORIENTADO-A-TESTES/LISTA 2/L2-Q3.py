'''3) Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à da
leitura.'''

def seed_lista(lista, tam):
    for i in range(tam):
        numero = int(input(f'Digite o {i+1} elemento da lista: '))
        lista.append(numero)


def main():
    while True:
        try:
            tamanho_lista = int(input('Digito o número de elementos da sequência: '))
            minha_lista = []
            while tamanho_lista <= 0:
                tamanho_lista = int(input('Número inválido. Por favor digite um número inteiro positivo: '))
            seed_lista(minha_lista, tamanho_lista)
            print(minha_lista[::-1])
            break

                
        except:
            print('\n------ Dado inválido!!! --------\n')    


main()
