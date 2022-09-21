''' 13) Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o
lançou n vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de
cada face.'''

from random import *

def joga_moeda(qtd):
   jogadas = []
   possibilidades = ['CARA', 'COROA']
   for i in range(qtd):
       jogadas.append(choice(possibilidades))
   return jogadas


def conta_resultados(ls_jogadas):
   qtd_cara = 0
   qtd_coroa = 0
   for jogada in ls_jogadas:
       if jogada == 'CARA':
           qtd_cara += 1
       else:
           qtd_coroa += 1
   print(f"A face CARA apareceu: {qtd_cara} veze(s)")
   print(f"A face COROA apareceu: {qtd_coroa} veze(s)")


def main():
   while True:
       try:
           quantidade_de_jogadas = int(input('Digite o número de vezes que deseja jogar a moeda: '))
           while quantidade_de_jogadas <= 0:
               print('Você digitou um número inválido...digite novamente.')
               quantidade_de_jogadas = int(input('Digite a quantidade de jogadas: '))
           jogo = joga_moeda(quantidade_de_jogadas)
           conta_resultados(jogo)
           break
       except ValueError:
           print('Erro! Você digitou um dado inválido! ')

main()
    
