'''17) Ler uma lista W de 10 elementos, depois ler um valor V. Contar e escrever quantas vezes o
valor V ocorre na lista W e escrever também em que posições (índices) da lista W o valor V
aparece.'''


from random import *

def criar_lista():
    ls = []
    for i in range(10):
        ls.append(randint(-999,999))
    return ls


def buscar_valor(vl_busca, lista_busca):
    contador = 0
    indices = []
    tam_lista = len(lista_busca)
    for index in range(tam_lista):
        if lista_busca[index] == vl_busca:
            contador += 1
            indices.append(index)
    if contador == 0:
        print(f'O valor {vl_busca} que deseja buscar não existe na lista')
    else:
        print(f'O valor {vl_busca} aparece {contador} veze(s) na lista')
        print(f'Os indices que eleparece são: {indices}')
  

def main():
    lista = criar_lista()
    while True:
        try:
            valor_de_busca = int(input('Digite o valor que deseja buscar: '))
            buscar_valor(valor_de_busca, lista)
            print('\n==================== LISTA GERADA ==============================\n')
            print(lista)
            break
        except:
            print('Você digitou um dado inválido, por favor, digite novamente... ')


main()
