
def eh_impar(n):
    return n % 2 != 0


def main():
    numero = float(input())
    print(f'{eh_impar(numero)}')


if __name__ == '__main__':
    main()
