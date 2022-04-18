

def tamanhoDoTexto(msg):
    return len(msg)


def main():
    texto = input()
    print(f'{tamanhoDoTexto(texto)}')


if __name__ == '__main__':
    main()


