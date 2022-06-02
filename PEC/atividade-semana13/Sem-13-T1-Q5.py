lista_A = []
lista_B = []

for _ in range(25):
    lista_A.append((int(input().strip())))

for _ in range(25):
    lista_B.append((int(input().strip())))

lista_C = []

for i in range(25):
    lista_C.append(lista_A[i])
    lista_C.append(lista_B[i])

print(lista_A)
print(lista_B)
print(lista_C)
