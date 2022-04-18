
def pagamento(valor):
    prestacao = valor/5
    desconto = valor * 0.91
    juros = (valor * 1.17)/10
    return f'{desconto:.2f}\n{prestacao:.2f}\n{juros:.2f}'


def main():
    valor_da_compra = float(input())
    print(pagamento(valor_da_compra))


if __name__ == '__main__':
    main()
