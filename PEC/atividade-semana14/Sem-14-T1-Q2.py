def sum_temperature(t1, t2):
    if t1[1] == t2[1]:
        t = t1[0] + t2[0]
        esc = t1[1]
        return t.__round__(4), esc
    elif t2[1] == 'F' and t1[1] == 'C':
        fahrenheit = (9 / 5 * t1[0]) + 32
        t = fahrenheit + t2[0]
        esc = t2[1]
        return t.__round__(4), esc
    elif t2[1] == 'C' and t1[1] == 'F':
        celsius = (5 / 9) * (t1[0] - 32)
        t = celsius + t2[0]
        esc = t2[1]
        return t.__round__(4), esc


temp = float(input())
escala = input().upper()[0]

tupla1 = (temp, escala)

temp = float(input())
escala = input().upper()[0]

tupla2 = (temp, escala)

print(sum_temperature(tupla1, tupla2))
