
tempo = 0

populacao_a = int(input().strip())

populacao_b = int(input().strip())


if populacao_b > populacao_a:
    aux = populacao_a
    populacao_a = populacao_b
    populacao_b = aux


while populacao_a > populacao_b:
     populacao_a = 1.02 * populacao_a
     populacao_b = 1.03 * populacao_b
     tempo += 1


print(tempo)
