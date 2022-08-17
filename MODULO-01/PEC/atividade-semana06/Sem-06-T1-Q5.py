
def main():
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())

    media = (nota1 + nota2 + nota3)/3
    if nota3 > 8:
        media += 1
        if media > 10:
            media = 10

    print(f'{media:.2f}')


if __name__ == '__main__':
    main()
