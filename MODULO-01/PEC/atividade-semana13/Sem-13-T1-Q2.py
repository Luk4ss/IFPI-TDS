n = int(input())

lista = []

for i in range(n):
    lista.append(0)

print(lista)
lista.clear()

for i in range(1, n + 1):
    lista.append(i)

print(lista)
lista.clear()

for i in range(n):
    lista.append(int(input().strip()))

print(lista)
lista.clear()

for i in range(n):
    lista.insert(0, int(input().strip()))

print(lista)
