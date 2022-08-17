
poupanca = 10000

preco_carro = int(input())

taxa_p = 0.7/100 + 1

taxa_c = 0.4/100 + 1

mes = 1


while poupanca*(taxa_p ** mes) < preco_carro*(taxa_c ** mes):
    mes += 1

print(mes)
