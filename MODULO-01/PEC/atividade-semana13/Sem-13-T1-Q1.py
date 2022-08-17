
numeros = []

for i in range(10):
    numeros.append(int(input().strip()))

acc = 1
for i in range(10):
    acc *= numeros[i]

print(numeros)
print(sum(numeros))
print(acc)
