alunos = []
idades = []
alturas = []

for _ in range(30):
    alunos.append(input().strip())
    idades.append(int(input().strip()))
    alturas.append(float(input().strip()))

media_alturas = (sum(alturas)/len(alturas)).__round__(2)

result = []

for i in range(30):
    if alturas[i] < media_alturas and idades[i] > 13:
        result.append(alunos[i])


print('MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA')
for student in result:
    print(student)
