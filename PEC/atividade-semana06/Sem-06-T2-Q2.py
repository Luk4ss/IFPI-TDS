
def is_letra(char):
    return 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122


def main():
    caractere = input()
    print(f'{is_letra(caractere)}')


if __name__ == '__main__':
    main()
