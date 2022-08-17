
# a a z => 97 a 122
# A a Z => 65 a 90
# 0 a 9 => 48 a 57

def is_letra_ou_numero(ctr):
    char_number = ord(ctr)
    return (48 <= char_number <= 57 or
            65 <= char_number <= 90 or
            97 <= char_number <= 122)


def main():
    letra = input()
    print(f'{is_letra_ou_numero(letra)}')


if __name__ == '__main__':
    main()
