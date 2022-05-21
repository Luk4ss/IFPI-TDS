
"""
Uma forma de fazer a questão é utilizando a equção horária do espaço. Igualando as duas equações (lebre e tartaruga)
podemos encontrar o tempo:

    v_tartaruga = 1

    v_lebre = 10

    #R Registra a posição inicial da tartaruga.
    posicao_tartaruga = int(input())

    # Essa variável é resultado da igualdade das duas equações horárias do espaço.
    tempo = (posicao_tartaruga)/(v_lebre - v_tartaruga)

    # A função ceil arredonda para cima.
    print(tempo.__ceil__())
"""


v_tartaruga = 1

v_lebre = 10

posicao_tartaruga = int(input())

posicao_lebre = 0

tempo = 0

while True:

    # Variável para representar a posição da tartaruga no instante t
    st =  posicao_tartaruga + v_tartaruga * tempo

    # Variável para representar a posição da lebre no instante t
    sl = v_lebre * tempo

    # Condição de parada.
    if st <= sl:
        break

    tempo += 1


print(tempo)
