
nomes = []

alturas = []


for _ in range(12):
    nomes.append(input().strip())
    alturas.append(float(input().strip()))

jogador_mais_alto = nomes[alturas.index(max(alturas))]
print('JOGADOR MAIS ALTO DO TIME')
print(jogador_mais_alto)
print(f'{max(alturas):.2f}')

if len(alturas):
    print('ALTURA MÉDIA DO TIME')
    media_altura = sum(alturas)/len(alturas)
    print(f'{media_altura:.2f}')
    print('JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME')
    for i in range(12):
        altura = alturas[i]
        if altura > media_altura:
            nome = nomes[i]
            print(f'{nome}')
            print(f'{altura:.2f}')
