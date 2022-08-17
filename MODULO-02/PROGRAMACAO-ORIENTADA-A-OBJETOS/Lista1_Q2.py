
def main():
    class Gato:
        nome = None
        raca = None
        idade = None
        peso = None
        sexo = None
        fertil = None
        cio = None
        prenhe = None
        puerperio = None

        def mudar_nome(self, nome):
            self.nome = nome

        def engordar(self, peso):
            self.peso += peso
            print(f'{self.nome} ganhou um pouco de peso. Agora seu peso é de {self.peso} kg')

        def envelhecer(self):
            self.idade += 1
            if self.idade >= 1:
                self.fertil = True
            print(f'{self.nome} envelheceu 1 ano. {self.nome} agora possui {self.idade} ano(s) de idade.')

        def entrar_no_cio(self):
            if self.idade >= 1 and self.sexo == "F":
                self.cio = True
                print(f'{self.nome} agora está no cio. ')

        def cruzar(self, gato):
            if type(gato) == type(Gato()):
                print(">>>>>>>> Processo de cruzamento iniciado...")
                if (self.sexo != gato.sexo) and (self.fertil and gato.fertil) and (
                        self.cio == True or gato.cio == True):
                    if self.puerperio != True and gato.puerperio != True:
                        print('>> O cruzamento foi um sucesso! Um(a) novo(a) gatinho(a) acaba de nascer :) <<')
                        if self.sexo == 'F':
                            self.prenhe = True
                            self.puerperio = True
                        else:
                            gato.prenhe = True
                            gato.puerperio = True
                        return Gato()

                print('>> FALHOU !!! Pelo menos um dos gatos envolvidos não está em condições de acasalar.')

            else:
                print('Por favor! Informe um gato em condições de acasalamento.')

    # Gato Felix
    felix = Gato()
    felix.nome = 'Felix'
    felix.sexo = 'M'
    felix.idade = 1
    felix.peso = 2.5
    felix.raca = 'siamês'

    felix.envelhecer()
    felix.engordar(0.5)

    # Gata Mel
    mel = Gato()
    mel.nome = 'Mel'
    mel.sexo = 'F'
    mel.idade = 1
    mel.peso = 2
    mel.raca = 'vira-lata'

    mel.envelhecer()
    mel.engordar(0.5)
    mel.entrar_no_cio()

    # Gato Garfield
    garfield = felix.cruzar(mel)

    garfield.nome = 'Garfield'
    garfield.sexo = 'M'
    garfield.idade = 0
    garfield.peso = 1.5
    garfield.raca = 'vira-lata'

    garfield.envelhecer()
    garfield.engordar(0.85)

    # Teste de parâmetros indevidos
    gato_a = mel.cruzar(felix)
    gato_b = felix.cruzar(2)


if __name__ == '__main__':
    main()
