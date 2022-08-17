
qtd_pares = 0

qtd_impares = 0

for _ in range(0, 100):
    numero = int(input())
    if numero % 2 == 0:
        qtd_pares += 1
    else:
        qtd_impares +=1

print(f'{qtd_pares}')
print(f'{qtd_impares}')
