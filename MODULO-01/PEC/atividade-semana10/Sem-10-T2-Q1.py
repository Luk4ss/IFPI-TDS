
soma = 0

num = int(input())

while num != 0:
    # soma = soma + num    ===  soma += num
    soma += num
    num = int(input())

print(f'{soma}')

