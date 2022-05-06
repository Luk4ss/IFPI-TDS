def maior(n1, n2):
    return n1 if n1 > n2 else n2


num = 0
result = 0

for _ in range(0, 100):
    num = int(input())
    result = (maior(result, num))


print(f'{result}')
