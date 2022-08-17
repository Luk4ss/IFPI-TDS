def contar(ls, num):
    ocorrencias = 0
    for elemento in ls:
        if elemento == num:
            ocorrencias += 1
    return ocorrencias


lista = []

while True:
    n = int(input().strip())
    if n == 0:
        break
    lista.append(n)

valor_buscado = int(input().strip())

if len(lista):
    print(lista)
    print(valor_buscado)
    print(contar(lista, valor_buscado))
