def is_primo(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        return print(num)



def main():
    a = int(input())
    b = int(input())

    if a > b:
        aux = a
        a = b
        b = aux

    for n in range(a, b + 1):
        is_primo(n)


if __name__ == '__main__':
    main()
