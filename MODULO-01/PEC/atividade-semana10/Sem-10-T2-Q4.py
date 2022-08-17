
opt = '5'
soma = 0.0

while opt != 'X':
    print('''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA''')

    opt = input().upper().strip()

    if opt == 'H':
        soma += 5.50

    elif opt == 'C':
        soma += 6.80

    elif opt == 'M':
        soma += 4.50

    elif opt == 'A':
        soma += 7.00

    elif opt == 'Q':
        soma += 4.00


print(f'{soma:.2f}')
