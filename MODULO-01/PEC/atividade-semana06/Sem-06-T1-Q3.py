

def main():

    cor = input()

    if cor == 'V' or cor == 'v':
        print('Siga')
    elif cor == 'A' or cor == 'a':
        print('Atenção')
    elif cor == 'E' or cor == 'e':
        print('Pare')
    else:
        print('entrada invalida')


if __name__ == '__main__':
    main()