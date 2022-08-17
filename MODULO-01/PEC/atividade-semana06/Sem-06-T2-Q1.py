
# a, e, i, o, u => 97, 101, 105, 111, 117
# A, E, I, O, U => 65, 69, 73, 79, 85
def is_vogal(ctr):
    char_number = ord(ctr)
    return (char_number == 97 or char_number == 65 or
            char_number == 101 or char_number == 69 or
            char_number == 105 or char_number == 73 or
            char_number == 111 or char_number == 79 or
            char_number == 117 or char_number == 85)


def main():
    letra = input()
    print(f'{is_vogal(letra)}')


if __name__ == '__main__':
    main()
