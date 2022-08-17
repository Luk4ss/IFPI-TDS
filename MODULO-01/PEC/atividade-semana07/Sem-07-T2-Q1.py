
try:
    nome = input().strip()
    estado_civil = int(input())
    if estado_civil == 1:
        nome_conjuge = input().strip()
        print(f'{len(nome + nome_conjuge)}')
    if estado_civil == 2:
        print(f'{len(nome)}')
except ValueError:
    print(f'Entrada inválida')