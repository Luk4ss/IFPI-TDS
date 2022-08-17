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


day = int(input())

month = int(input())

cidades = carrega_cidades()

meses = ('JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO',
         'NOVEMBRO', 'DEZEMBRO')

print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {day} DE {meses[month - 1]}:')
for cidade in cidades:
    if cidade[3] == day and cidade[4] == month:
        print(f'{cidade[2]}({cidade[0]})')
