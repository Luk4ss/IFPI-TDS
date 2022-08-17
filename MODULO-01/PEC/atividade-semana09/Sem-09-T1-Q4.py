

num = 0

while num < 1000:
    num += 10
    if num == 1000:
        print(f'{num}', end='.')
    else:
        print(f'{num}', end=', ')

