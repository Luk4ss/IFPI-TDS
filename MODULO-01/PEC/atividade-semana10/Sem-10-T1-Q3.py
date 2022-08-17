def maior(n1, n2):
    return n1 if n1 > n2 else n2


def menor(n1, n2):
    return n1 if n1 < n2 else n2


major = -999999999

minor = 999999999


while True:
    n = int(input())
    if n == 0:
        break
    else:
        major = maior(n, major)
        minor = menor(n, minor)

if major != -999999999 or minor != 999999999:
    print(major)
    print(minor)
