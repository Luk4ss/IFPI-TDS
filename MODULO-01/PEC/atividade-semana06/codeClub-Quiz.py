

def main():
    score = 0

    print('Qual é o nome do fundador da Microsoft?\na-Bill Gates \nb-Steve Jobs \nc-Linus Torvalds')
    resposta = input('alternativa: ').strip().lower()

    if resposta == 'a':
        score += 1
        print('Parabéns! Você acertou!!! :)\n')
    elif resposta == 'b' or resposta == 'c':
        print('Você errou... :( \n')
    else:
        print('Você não respondeu uma alternativa válida\n')

    print('Qual é o nome do fundador da Apple?\na-Bill Gates \nb-Steve Jobs \nc-Linus Torvalds')
    resposta = input('alternativa: ').strip().lower()

    if resposta == 'b':
        score += 1
        print('Parabéns! Você acertou!!! :)\n')
    elif resposta == 'a' or resposta == 'c':
        print('Você errou... :( \n')
    else:
        print('Você não respondeu uma alternativa válida\n')

    print('Qual é o nome do criador do Linux?\na-Bill Gates \nb-Steve Jobs \nc-Linus Torvalds')
    resposta = input('alternativa: ').strip().lower()

    if resposta == 'c':
        score += 1
        print('Parabéns! Você acertou!!! :)\n')
    elif resposta == 'a' or resposta == 'b':
        print('Você errou... :( \n')
    else:
        print('Você não respondeu uma alternativa válida\n')

    print('Python é uma linguagem: \na-Compilada \nb-Interpretada \nc-pseudo-linguagem')
    resposta = input('alternativa: ').strip().lower()

    if resposta == 'b':
        score += 1
        print('Parabéns! Você acertou!!! :)\n')
    elif resposta == 'a' or resposta == 'b':
        print('Você errou... :( \n')
    else:
        print('Você não respondeu uma alternativa válida\n')

    print(f'Pontuação final: {score}\n')
    if score == 4:
        print('Muito bem! Você acertou todas as perguntas!')
    elif score == 0:
        print('Tente novamente...')
    else:
        print('Tente novamente e tente acertar todas as perguntas. Dessa vez você consegue!')


if __name__ == '__main__':
    main()
