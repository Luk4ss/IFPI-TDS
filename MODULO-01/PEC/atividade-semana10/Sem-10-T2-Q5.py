

nota = -1

while not (0.0 <= nota <= 10.0):
    nota = float(input())
    if 0.0 <= nota < 4:
        print('E')
        flag = False

    elif 4 <= nota < 5:
        print('D')

    elif 5 <= nota < 7:
        print('C')

    elif 7 <= nota < 8.5:
        print('B')

    elif 8.5 <= nota <= 10:
        print('A')

    else:
        print('Nota inválida.')
