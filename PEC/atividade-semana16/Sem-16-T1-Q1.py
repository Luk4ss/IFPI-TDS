livros = {}
chave_inicial = 101

while True:
    titulo = input().strip()
    if not titulo:
        break
    isbn = input().strip()
    autor = input().strip()
    preco = float(input())
    livros[chave_inicial] = [titulo, isbn, autor, preco]
    chave_inicial += 1

for codigo in livros:
    print(f'Código: {codigo}')
    print(f'Título: {livros[codigo][0]}')
    print(f'ISBN: {livros[codigo][1]}')
    print(f'Autor: {livros[codigo][2]}')
    print(f'Preço: {livros[codigo][3]:.2f}')
