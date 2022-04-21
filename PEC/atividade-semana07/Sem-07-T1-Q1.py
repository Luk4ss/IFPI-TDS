dia = int(input().strip())
mes = int(input().strip())
ano = int(input().strip())

dia_nascimento = int(input().strip())
mes_nascimento = int(input().strip())
ano_nascimento = int(input().strip())

idade = ano - ano_nascimento

if mes < mes_nascimento:
    idade -= 1
elif dia < dia_nascimento:
    idade -= 1

print(idade)
