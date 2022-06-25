def calculaMedia(dados, codigo):
    media = (dados[codigo][1] + dados[codigo][2])/2
    return f'{dados[codigo][0]}: {media.__round__(1)}'


alunos = {}

while True:
    matricula = input().strip()
    if not matricula:
        break
    nome = input().strip()
    nota1 = float(input())
    nota2 = float(input())
    alunos[matricula] = [nome, nota1, nota2]


while True:
    codigo_aluno = input().strip()
    if not codigo_aluno:
        break
    print(calculaMedia(alunos, codigo_aluno))
