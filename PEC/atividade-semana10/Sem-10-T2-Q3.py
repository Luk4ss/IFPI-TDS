
opt = 1

while opt != 0:
    print('OPÇÕES: ')
    print('1 - SAUDAÇÃO\n2 - BRONCA\n3 - FELICITAÇÃO\n0 - FIM')
    opt = int(input())
    if opt == 1:
        print('1 - Olá. Como vai?')

    elif opt == 2:
        print('2 - Vamos estudar mais.')

    elif opt == 3:
        print('3 - Meus Parabéns!')

    elif opt == 0:
        print('0 - Fim de serviço.')

    else:
        print('Opção inválida.')
