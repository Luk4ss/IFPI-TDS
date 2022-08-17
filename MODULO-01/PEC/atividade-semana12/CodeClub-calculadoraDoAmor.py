
print('''CALCULADORA DO AMOR  
<3 <3 <3 <3 <3 <3 <3''')
nome1, nome2 = input("Escreva o nome de duas pessoas com o sinal '+' Exemplo (Rafael+Ana): ").split('+')


def calc_pontos(name1, name2):
    placar = 0
    for letra in name1:
        if letra in "aeiou":
            placar += 5
        if letra in "amor":
            placar += 10

    for letra in name2:
        if letra in "aeiou":
            placar += 5
        if letra in "amor":
            placar += 10

    return placar


pontos = calc_pontos(nome1, nome2)

if pontos < 10:
    print("Vocês são incompatíveis... É melhor tentar outra pessoa!")

elif pontos <= 30:
    print("Vocês se dão bem, mas a chance de serem somente amigos é muito grande.")

elif pontos <= 50:
    print("Vocês são muito próximos, se dão excepcionalmente bem. A chance de darem certo é altíssima!")

else:
    print("Vocês são almas gêmeas! Aproveite pois isso é raro!")
