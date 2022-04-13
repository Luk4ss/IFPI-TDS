
def is_digit(n):
    return 48 <= ord(n) <= 57


def main():
    digit = input()

    print(f'{is_digit(digit)}')


if __name__ == '__main__':
    main()
