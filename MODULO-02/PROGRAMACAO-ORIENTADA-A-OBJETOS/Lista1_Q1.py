
def main():
    class Carro:
        nome = None
        ano = None
        cor = None
        estado = None
        velocidade_atual = None
        velocidade_maxima = None

        def ligar(self):
            estado = True
            print(f'O(A) {self.nome} está ligado(a)')

        def desligar(self):
            estado = False
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

    fusca = Carro()
    fusca.nome = 'Fusca'
    fusca.ano = 1965
    fusca.cor = 'preto'
    fusca.velocidade_maxima = 80
    fusca.velocidade_atual = 20
    fusca.estado = True

    ferrari = Carro()
    ferrari.nome = 'Ferrari_sr2000'
    ferrari.ano = 2014
    ferrari.cor = 'vermelho'
    ferrari.velocidade_maxima = 300
    ferrari.velocidade_atual = 0
    ferrari.estado = False

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
