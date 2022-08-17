
def main():
    nome = input()
    sexo = int(input())

    if sexo == 1:
        print(f'Ilmo Sr. {nome}')
    elif sexo == 2:
        print(f'Ilma Sra. {nome}')

    else:
        print('invalido.')


if __name__ == '__main__':
    main()
