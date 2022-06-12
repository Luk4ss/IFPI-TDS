def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado


cidades = carrega_cidades()

month = int(input())

population = int(input())

meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
         'novembro', 'dezembro')

msg = f'CIDADES COM MAIS DE {population} HABITANTES E ANIVERSÁRIO EM {meses[month - 1]}:'

print(msg.upper())

for cidade in cidades:
    if cidade[4] == month and cidade[5] > population:
        print(f'{cidade[2]}({cidade[0]}) tem {cidade[5]} habitantes e faz aniversário em {cidade[3]}'
              f' de {meses[cidade[4] - 1]}.')
