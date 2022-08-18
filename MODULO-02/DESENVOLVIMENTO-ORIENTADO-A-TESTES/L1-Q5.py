# LISTA 1 - QUESTÃO 5

def peso_ideal(sexo, h):
  if sexo == 2:
    return (72.7 * h) - 58
  if sexo == 1:
    return (62.1 * h) - 44.7


while True:
  try:
    print('''Digite o seu sexo:
            1 - Feminino
            2 - Masculino ''')
    opcao = int(input('Sua opção: '))
    while opcao != 1 and opcao != 2:
        print('>> Opção inválida!! Digite a opção novamente.')
        opcao = int(input('Sua opção: '))
        if opcao in[1, 2]:
          break
    altura = float(input('Digite a sua altura: '))
    break
  except:
    print(">>>>> Valor inválido. Por favor, Digite novamente\n")

print(f'Seu peso ideal é: {peso_ideal(opcao, altura):.2f} kg')
