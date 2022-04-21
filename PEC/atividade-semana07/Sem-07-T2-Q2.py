
try:
    num = int(input())
    qtd_pares = 0

    u = num % 10
    d = (num % 100) // 10
    c = num // 100
    if u % 2 == 0:
        qtd_pares += 1
    if d % 2 == 0:
        qtd_pares += 1
    if c % 2 == 0 and c != 0:
        qtd_pares += 1
    print(qtd_pares)

except ValueError:
    print('Entrada inválida!')
