num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())


media = (num1 + num2 + num3 + num4 + num5)/5

print(f'{media:.2f}')

if num1 > media:
    print(num1)
if num2 > media:
    print(num2)
if num3 > media:
    print(num3)
if num4 > media:
    print(num4)
if num5 > media:
    print(num5)
