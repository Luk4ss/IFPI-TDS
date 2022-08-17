
opt = True
media = 0.0
soma = 0.0
qtd_loops = 0.0

while opt:
    n = int(input())
    if n == 0:
        opt = False
    else:
        qtd_loops += 1
        soma += n

if qtd_loops != 0:
    print(f'{soma/qtd_loops: .2f}')

