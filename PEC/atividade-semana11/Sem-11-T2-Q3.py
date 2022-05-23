
def soma_inversa(n, acc=1, total=0):
    total += 1/acc
    if acc == n:
        return total
    else:
        acc += 1
        return soma_inversa(n, acc, total)


def main():
    print(f'{soma_inversa(int(input())):.4f}')


if __name__ == '__main__':
    main()
