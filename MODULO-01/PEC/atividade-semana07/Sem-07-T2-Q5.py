num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 > num2 > num3:
    print(f'{num3}\n{num2}\n{num1}')
elif num1 > num3 > num2:
    print(f'{num2}\n{num3}\n{num1}')
elif num2 > num1 > num3:
    print(f'{num3}\n{num1}\n{num2}')
elif num2 > num3 > num1:
    print(f'{num1}\n{num3}\n{num2}')
elif num3 > num1 > num2:
    print(f'{num2}\n{num1}\n{num3}')
else:
    print(f'{num1}\n{num2}\n{num3}')
