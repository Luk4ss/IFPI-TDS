# LISTA 1 - QUESTÃO 10

def max(a, b, c, d ):
   maior = a
   if b >= maior:
     maior = b
   if c >= maior:
     maior = c
   if d >= maior:
     maior = d
   return maior


for i in range(1, 5):
    while True:
        print(f' >>> Série No#{i} <<<')
        try:
            a = int(input('Número 1: '))
            b = int(input('Número 2: '))
            c = int(input('Número 3: '))
            d = int(input('Número 4: '))
            break
        except:
            print('### Dado inválido! Por favor, digite novamente! ###\n')
    print(f'>>>> O maior número dessa série é: {max(a, b, c, d)}\n')
