num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())


def maior(n1, n2, n3, n4, n5):
    if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
        return n1
    elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
        return n2
    elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
        return n3
    elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
        return n4
    return n5


def menor(n1, n2, n3, n4, n5):
    if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5:
        return n1
    elif n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
        return n2
    elif n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
        return n3
    elif n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5:
        return n4
    return n5


print(f'{maior(num1, num2, num3, num4, num5)}')
print(f'{menor(num1, num2, num3, num4, num5)}')
