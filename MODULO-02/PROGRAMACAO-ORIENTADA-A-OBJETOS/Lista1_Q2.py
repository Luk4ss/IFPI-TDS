from random import *


def main():

    populacao_gatos = []

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

        def __init__(self, nome, sexo, peso, idade, raca):
            self.nome = nome
            self.peso = peso
            self.sexo = sexo
            self.idade = idade
            self.raca = raca

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
            if type(gato) == type(self):
                print(">>>>>>>> Processo de cruzamento iniciado...")
                if (self.sexo != gato.sexo) and (self.fertil and gato.fertil) and (
                        self.cio == True or gato.cio == True):
                    if self.puerperio != True and gato.puerperio != True:
                        if self.sexo == 'F':
                            self.prenhe = True
                        else:
                            gato.prenhe = True
                        return '>>> O cruzamento foi um sucesso! Novos filhotinhos estão por vir :) <<<'

                return '!!! FALHOU !!! Pelo menos um dos gatos envolvidos não está em condições de acasalar...'

            return 'Por favor! Informe um animal do tipo gato...'

        def parir(self):
            if self.sexo == 'F' and self.prenhe:
                self.puerperio = True
                self.prenhe = False
                filhotes = []
                qtd_filhotes = randint(1, 8)
                print(f'Quantidade de filhotes que nasceram : {qtd_filhotes}')
                for i in range(qtd_filhotes):
                    print(f'\n >>>> Dados do Filhote #{i + 1} <<<<')
                    sexo_filhote = choice(['F', 'M'])
                    peso_filhote = random().__round__(2)
                    print(f'Sexo do filhote: {sexo_filhote}')
                    nome_filhote = input('Digite o nome do filhote: ')
                    raca_filhote = choice(['Siamês', 'Vira-lata', 'Persa', 'Angorá', 'Ragdoll'])
                    filhotinho = Gato(nome_filhote, sexo_filhote, peso_filhote, 0, raca_filhote)
                    filhotes.append(filhotinho)
                    populacao_gatos.append(filhotinho)
                return filhotes

            return 0

    # Gato Felix
    felix = Gato('Félix', 'M', 2.5, 1, 'siamês')
    felix.envelhecer()
    felix.engordar(0.5)
    populacao_gatos.append(felix)

    # Gata Mel
    mel = Gato('Mel', 'F', 2.0, 1, 'vira-lata')
    mel.envelhecer()
    mel.engordar(0.5)
    mel.entrar_no_cio()
    populacao_gatos.append(mel)

    # Gato Garfield
    print(mel.cruzar(felix))
    ninhada = mel.parir()


    print('\n >>>> TODOS OS FILHOTES <<<<')
    for filhote in ninhada:
        print(f'Filhote >>> Nome: {filhote. nome}, Sexo: {filhote.sexo}, Raça: {filhote.raca}, Peso: {filhote.peso} kg')

    # Teste de parâmetros indevidos
    print('-------------------------------------')
    print(mel.cruzar(felix))
    print('-------------------------------------')
    print(felix.cruzar(2))
    print('-------------------------------------')

    # Imprime toda a população de gatos
    print(' >>>>>> POPULAÇÃO DE GATOS <<<<<<< ')
    for gato in populacao_gatos:
        print(f'Nome: {gato.nome}, sexo: {gato.sexo}, idade: {gato.idade}, raça: {gato.raca}')

if __name__ == '__main__':
    main()
