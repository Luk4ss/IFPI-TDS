n = int(input())

lista = []





if n != 0:
    for i in range(n):
        lista.append(float(input().strip()))

    print(lista[::-1])

    lista.clear()
    for i in range(n):
        lista.append(float(input().strip()))

    print(lista)
    media = sum(lista)/len(lista)
    print(f'{media:.1f}')

    lista.clear()
    for i in range(n):
        lista.append(input()[0])

    count = 0

    if lista.__contains__('a'):
        count += 1
        lista.remove('a')
    if lista.__contains__('A'):
        count += 1
        lista.remove('A')

    if lista.__contains__('e'):
        count += 1
        lista.remove('e')
    if lista.__contains__('E'):
        count += 1
        lista.remove('E')

    if lista.__contains__('i'):
        count += 1
        lista.remove('i')
    if lista.__contains__('I'):
        count += 1
        lista.remove('I')

    if lista.__contains__('o'):
        count += 1
        lista.remove('o')
    if lista.__contains__('O'):
        count += 1
        lista.remove('O')

    if lista.__contains__('u'):
        count += 1
        lista.remove('u')
    if lista.__contains__('U'):
        count += 1
        lista.remove('U')
    print(count)
    print(lista)

else:
    print(lista)
    print(lista)
    print("SEM NOTAS")
    print(0)
    print(lista)


# Tentei com esse bloco de código para checar as vogais mas tirei 9.0  e o caso 8 não possui entrada de teste disponível:/
"""
    for element in lista:
        if element == 'a' or element == 'A':
            count += 1
            lista.remove(element)
        elif element == 'e' or element == 'E':
            count += 1
            lista.remove(element)
        elif element == 'i' or element == 'I':
            count += 1
            lista.remove(element)
        elif element == 'o' or element == 'O':
            count += 1
            lista.remove(element)
        elif element == 'u' or element == 'U':
            count += 1
            lista.remove(element)
"""