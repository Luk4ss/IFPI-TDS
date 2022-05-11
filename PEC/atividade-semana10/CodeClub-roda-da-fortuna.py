from random import *

# Imprime na tela as três portas e as instruções do jogo.
print('''
Gameshow!
=========

Há um prêmio escondido atrás de uma dessas 3 portas!
Escolha a porta correta para ganhar o prêmio!
  _____   _____   _____
 |     | |     | |     |
 | [1] | | [2] | | [3] |
 |   o | |   o | |   o |
 |_____| |_____| |_____|
 
Se você acertar, você ganha +1 ponto, porém se errar você terá seus pontos ZERADOS, então CUIDADO!
Você pode tentar quantas vezes quiser. Para sair do jogo digite o caractere 'n'. 
''')

score = 0
play = "s"

# Repete o jogo enquanto o usuário não digitar o caractere 'n'

while play != 'n':
    print("\nChoose a door (1, 2 or 3):")

    # lê no teclado um número e o converte para o tipo inteiro
    chosenDoor = int(input())

    # Gera um número inteiro randômico entre 1 e 3
    winningDoor = randint(1, 3)

    # Mostra qual porta foi escolhida e qual porta é a correta.
    print("A porta escolhida foi: ", chosenDoor)
    print("A porta com o correta é: ", winningDoor)

    # Verifica se o jogador acertou ou errou a porta que contém o prêmio.
    if chosenDoor == winningDoor:
        print("Muito bem! Você acertou!")
        score += 1

    else:
        print("Não foi dessa vez... :(")
        score = 0

    print("\nSua pontuação:", score)
    print("Você gostaria de continuar jogando (s/n) ?")
    play = input().strip().lower()
    if play == 'n':
        print("\nSua pontuação final é: ", score)
        if score >= 3:
            print('Você foi muito bem!')
        else:
            print('Foi um bom jogo, porém poderia ser melhor...')
