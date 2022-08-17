
def is_primo(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    return True if count == 2 else False


def main():
    print(is_primo(int(input())))


if __name__ == '__main__':
    main()
