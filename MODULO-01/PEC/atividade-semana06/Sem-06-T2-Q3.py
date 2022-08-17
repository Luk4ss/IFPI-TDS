
# a, e, i, o, u => 97, 101, 105, 111, 117
# A, E, I, O, U => 65, 69, 73, 79, 85

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
    letra = input()
    print(f'{is_consoante(letra)}')


if __name__ == '__main__':
    main()
