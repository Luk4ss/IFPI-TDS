agenda = {}

tamanho_agenda = int(input())

for i in range(1, tamanho_agenda + 1):
    nome = input().strip()
    cidade = input().strip()
    estado = input().strip()
    telefone = input().strip()
    agenda[i] = [nome, cidade, estado, telefone]


for contato in agenda:
    cidade_estado = agenda[contato][1] + '(' + agenda[contato][2] + ')'
    print(f'{agenda[contato][0]:25}{cidade_estado:30}{agenda[contato][3]:10}')
