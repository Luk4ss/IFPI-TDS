'''12) Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. A
prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E.
Para isso são dados:
o cartão gabarito;
o número de alunos da turma;
o cartão de respostas para cada aluno, contendo o seu número e suas respostas.'''


from random import *

def gera_gabarito():
    gab = []
    alternativas = ['A', 'B', 'C', 'D', 'E']
    for i in range(30):
        gab.append(choice(alternativas))
    return gab


def gera_lista_alunos(qtd):
    n_alunos = list(range(qtd))
    return n_alunos

def gera_respostas_para_aluno(ls_alunos):
    alternativas = ['A', 'B', 'C', 'D', 'E']
    aluno_resposta = []
    for i in range(len(ls_alunos)):
        resposta = gera_gabarito()
        aluno = ls_alunos[i]
        aluno_resposta.append([aluno, resposta])
    return aluno_resposta

def main():
    gabarito = gera_gabarito()
    while True:
        try:
          qtd_alunos = int(input('Digite um número: '))
          while qtd_alunos <= 0:
              print('Você digitou um número inválido... .')
              qtd_alunos = int('Digite novamente a quantidade de alunos: ')
          alunos = gera_lista_alunos(qtd_alunos)
          respostas_por_aluno = gera_respostas_para_aluno(alunos)
          print("============= GABARITO =============")
          print(gabarito)
          print("=========== RESPOSTAS POR ALUNO =========")
          for al_resposta in respostas_por_aluno:
              print(f"RESPOSTAS DO ALUNO {al_resposta[0]}:\n{al_resposta[1]}")
          break
        except ValueError:
          print("Você digitou um dado inválido...")
    

main()

