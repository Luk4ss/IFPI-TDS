def is_letra(char):
    return 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122


def is_numero(char):
    return 48 <= ord(char) <= 57


def is_vogal(char):
    char_number = ord(char)
    return (char_number == 97 or char_number == 65 or
            char_number == 101 or char_number == 69 or
            char_number == 105 or char_number == 73 or
            char_number == 111 or char_number == 79 or
            char_number == 117 or char_number == 85)


def is_consoante(ctr):
    char_number = ord(ctr)
    return (65 < char_number < 69 or
            69 < char_number < 73 or
            73 < char_number < 79 or
            79 < char_number < 85 or
            85 < char_number <= 90 or
            97 < char_number < 101 or
            105 < char_number < 111 or
            111 < char_number < 117 or
            117 < char_number <= 122)


def main():
    entrada = input()

    if is_numero(entrada):
        print('número')

    elif is_letra(entrada):
        if is_vogal(entrada):
            print('vogal')
        elif is_consoante(entrada):
            print('consoante')

    else:
        print('símbolo')


if __name__ == '__main__':
    main()
