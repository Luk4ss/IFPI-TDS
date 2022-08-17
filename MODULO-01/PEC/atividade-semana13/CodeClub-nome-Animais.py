from random import *


nomes = ["Nina", "Lulu", "Valentina", "Rex", 'chico', 'Arisca', 'cateto', 'hipotenusa']

print("GERADOR DE NOMES PARA ANIMAIS")
print("-----------------------------")

while True:
    print('''Menu
    a - obter nome
    b - adicionar um nome
    c - remover um nome
    d - imprimir nomes
    e - sair
    ''')

    opt = input('Opção: ').strip()[0]
    if opt == 'e':
        break

    elif opt == 'a':
        print('      Você deve chamar seu animal de estimação de ' + choice(nomes))

    elif opt == 'b':
        print('Digite o nome que deseja adiconar: ')
        h = input().strip()
        if h in nomes:
            print('Esse nome já existe!')
        else:
            print('Nome adicionado com sucesso!')
            nomes.append(input().strip())

    elif opt == 'c':
        print('Digite o nome que deseja remover: ')
        nomes.remove(input().strip())

    elif opt == 'd':
        print('Todos os hobbies: ')
        print(nomes)
