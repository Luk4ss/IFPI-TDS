deposito = float(input())
taxa = float(input()) / 100
tempo = 0
poupanca = 0.0

while poupanca < 2*deposito:
    tempo += 1
    poupanca = deposito*(1 + taxa)**tempo


print(tempo)

