

def main():
    birthday = input().strip()
    soma = 0
    for i in range(len(birthday)):
        soma += int(birthday[i])

    print(soma)


if __name__ == '__main__':
    main()
