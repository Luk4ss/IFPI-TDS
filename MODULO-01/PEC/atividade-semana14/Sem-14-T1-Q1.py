def higher_temperature(t1, t2):
    if t1[1] == t2[1]:
        return t1 if t1[0] > t2[0] else t2
    elif t1[1] == 'F':
        celsius = (5/9) * (t1[0] - 32)
        return t1 if celsius > t2[0] else t2
    elif t1[1] == 'C':
        fahrenheit = (9/5 * t1[0]) + 32
        return t1 if fahrenheit > t2[0] else t2
    elif t2[1] == 'F':
        celsius = (5/9) * (t1[0] - 32)
        return t2 if celsius > t1[0] else t1
    elif t2[1] == 'C':
        fahrenheit = (9/5 * t1[0]) + 32
        return t2 if fahrenheit > t1[0] else t1


temp = float(input())
escala = input().upper()[0]

tupla1 = (temp, escala)

temp = float(input())
escala = input().upper()[0]

tupla2 = (temp, escala)

print(higher_temperature(tupla1, tupla2))
