try:
    num = int(input())
    qtd_impares = 0

    if 10 <= num <= 99:
        u = num % 10
        d = num // 10
        if u % 2 != 0:
            qtd_impares += 1
        if d % 2 != 0:
            qtd_impares += 1

        if qtd_impares == 0:
            print('Nenhum dígito é ímpar.')
        elif qtd_impares == 1:
            print('Apenas um dígito é ímpar.')
        elif qtd_impares == 2:
            print('Os dois dígitos são ímpares.')

except ValueError:
    print('Entrada inválida!')
