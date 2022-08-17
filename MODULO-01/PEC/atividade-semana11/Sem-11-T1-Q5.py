
populacao = int(input().strip())

ano = 1600

populacao_original = populacao

while populacao >= 0.1 * populacao_original:

    nascituro = 0.01 * populacao

    falecidos = 0.06 * populacao

    populacao = populacao + nascituro - falecidos

    print(f'{ano:.0f},{nascituro:.0f},{falecidos:.0f},{populacao:.0f}')

    ano += 1

