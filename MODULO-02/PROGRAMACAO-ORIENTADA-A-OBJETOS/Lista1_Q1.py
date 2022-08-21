
def main():
    class Carro:

        def __init__(self, nome, ano, cor, velocidade_maxima):
            self.nome = nome
            self.ano = ano
            self.cor = cor
            self.velocidade_maxima = velocidade_maxima
            self.velocidade_atual = 0
            self.estado = False

        def ligar(self):
            self.estado = True
            print(f'O(A) {self.nome} está ligado(a)')

        def desligar(self):
            self.estado = False
            self.velocidade_atual = 0
            print(f'O(A) {self.nome} está desligado(a)')

        def parar(self):
            self.velocidade_atual = 0
            print(f'A velocidade atual do(a) {self.nome} é de {self.velocidade_atual} km/h')

        def acelerar(self, velocidade):
            if self.estado:
                if (self.velocidade_atual + velocidade) >= self.velocidade_maxima:
                    self.velocidade_atual = self.velocidade_maxima
                else:
                    self.velocidade_atual += velocidade
                print(f'A velocidade atual do(a) {self.nome} é: {self.velocidade_atual} km/h')
            else:
                print('Não é possível acelerar com o carro desligado.')

    fusca = Carro('Fusca', 1965, 'preto', 80)
    fusca.ligar()
    fusca.velocidade_atual = 20

    ferrari = Carro('Ferrari_sr2000', 2014, 'vermelho', 300)


    # letra a)
    fusca.acelerar(20)

    # letra b)
    ferrari.acelerar(200)

    # letra c)
    fusca.desligar()

    # letra d)
    ferrari.ligar()

    # letra e)
    ferrari.acelerar(320)

    # letra f)
    ferrari.parar()

    # letra g)
    ferrari.desligar()

    # letra h)
    fusca.ligar()

    # letra i)
    fusca.acelerar(100)

    # letra j)
    fusca.desligar()


if __name__ == '__main__':
    main()
