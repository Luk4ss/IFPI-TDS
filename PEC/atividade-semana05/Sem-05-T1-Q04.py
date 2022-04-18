
def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    maior = max(a, b, c, d, e)
    menor = min(a, b, c, d, e)
    media = (a + b + c + d + e)/5

    print(f'{maior}\n{menor}\n{media:.1f}')


if __name__ == '__main__':
    main()
