agenda = {}
menores = {}

for i in range(1, 21):
    nome = input().strip()
    idade = int(input().strip())
    cpf = input().strip()
    agenda[i] = [nome, idade, cpf]


for i in range(1, 21):
    if agenda[i][1] < 18:
        menores[i] = agenda[i]
        del agenda[i]


print('========== MAIORES DE 18 ANOS ==========')
for contato in agenda:
    print(f'{agenda[contato][0]};{agenda[contato][1]};{agenda[contato][2]}')
print('========== MENORES DE 18 ANOS ==========')
for contato in menores:
    print(f'{menores[contato][0]};{menores[contato][1]};{menores[contato][2]}')
