
def fatorial(n, acc=1):
    if n == 0:
        n = 1
    acc *= n
    return fatorial(n - 1, acc) if n > 1 else acc


def main():
    print(fatorial(int(input())))


if __name__ == '__main__':
    main()
