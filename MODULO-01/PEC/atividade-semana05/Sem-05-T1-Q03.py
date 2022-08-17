
def relogio(segundos):
    horas = segundos // 3600
    segundos = segundos % 3600
    minutos = segundos // 60
    segundos = segundos % 60
    return f'{horas}:{minutos}:{segundos}'


def main():
    tempo_de_duracao = int(input())
    print(relogio(tempo_de_duracao))


if __name__ == '__main__':
    main()
