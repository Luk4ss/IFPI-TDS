from random import *

adjetivos = ["maravilhosa", "acima da média", "educada", "excelente", "inteligente"]
hobbies = ["fazer caminhada", "programar", "fazer café", "ensinar"]

print("GERADOR DE CUMPRIMENTOS")
nome = input("Qual é o seu nome?: ").strip()

print(nome, "você é uma pessoa", choice(adjetivos), "em", choice(hobbies))
print("De nada!")

while True:
    print('''Menu
    a - obter cumprimento
    b - adicionar um hobby
    c - remover um hobby
    d - imprimir hobbies
    e - sair
    ''')

    opt = input('Opção: ').strip()[0]
    if opt == 'e':
        break

    elif opt == 'a':
        print(nome, "você é uma pessoa", choice(adjetivos), "em", choice(hobbies))
        print("De nada!")

    elif opt == 'b':
        print('Digite o hobby que deseja adiconar: ')
        h = input().strip()
        if h in hobbies:
            print('Esse hobby já existe!')
        else:
            print('Hobby adicionado com sucesso!')
            hobbies.append(input().strip())

    elif opt == 'c':
        print('Digite o hobby que deseja remover: ')
        hobbies.remove(input().strip())

    elif opt == 'd':
        print('Todos os hobbies: ')
        print(hobbies)
