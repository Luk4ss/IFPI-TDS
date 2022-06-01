par = []
impar = []
numeros = []

for _ in range(20):
    n = int(input().strip())
    numeros.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)


print(numeros)
print(par)
print(impar)
