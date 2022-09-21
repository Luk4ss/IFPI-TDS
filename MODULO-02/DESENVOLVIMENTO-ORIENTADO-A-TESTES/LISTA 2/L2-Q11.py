''' 11) Faça um programa que alimente uma lista com um número de posições definidas pelo
usuário. Esta lista deverá armazenar um conjunto de nomes em diferentes posições.
Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente. '''


def criar_lista(n_posicao):
    lista = [0] * n_posicao
    print(f"Uma lista com tamanho {n_posicao} foi gerada.")
    return lista


def cadastrar_nome(nome, ls_nomes):
    tam_lista = len(ls_nomes)
    for i in range(tam_lista):
        if ls_nomes[i] == 0:
           ls_nomes[i] = nome
           return True
    return False     


def pesquisar_nome(nome, ls_nomes):
    resultado_pesquisa = -1
    for n in ls_nomes:
        if n == nome:
           resultado_pesquisa = nome, True
           return resultado_pesquisa
    resultado_pesquisa = None, False
    return -1, False 

def deletar_nome(excluir, ls_nomes):
    tam_lista = len(ls_nomes)
    for i in range(tam_lista):
        if ls_nomes[i] == excluir:
            ls_nomes[i] = 0
            return True
    return False

def mostrar_nomes(ls_nomes):
    flag = True
    for nome in ls_nomes:
        if nome != 0:
           flag = False
           print(nome)
    if flag:
        print("--- A Lista está vazia ----")

def main():
    while True:
        try:
            tamanho = int(input("Digite o tamanho da lista que deseja criar: "))
            lista_nomes = criar_lista(tamanho)
            break
        except:
            print('Você digitou um dado inválido! Digite novamente... ')
    while True:    
        print('''========= MENU ========
        1) Cadastrar Nome
        2) Pesquisar Nome
        3) Listar todos os nomes
        4) Deletar Nome
        0) Sair do programa''')
        opcao = input('Digite a sua escolha: ')
        if opcao == '1':
            nome_cadastro = input('Digite o nome que deseja cadastrar: ').strip().upper()
            if cadastrar_nome(nome_cadastro, lista_nomes):
                print("Nome cadastrado com sucesso! ")
            else:
                print("Não é possível cadastrar mais nomes pois a lista está cheia! ")
        elif opcao == '2':
            pesquisa = input('Digite o nome que deseja pesquisar: ').strip().upper()
            resultado, flag = pesquisar_nome(pesquisa,lista_nomes)
            if flag:
               print(f'>>> O Nome {resultado} foi encontrado.')
            else:
               print(f">>> O nome {pesquisa} não existe na lista...")
        elif opcao == '3':
            print("========== TODOS OS NOMES DA LISTA ===========")
            mostrar_nomes(lista_nomes)
            print("==============================================")
        elif opcao == '4':
            nome_exclusao = input("Digite o nome que deseja excluir da lista: ").strip().upper()
            if(deletar_nome(nome_exclusao, lista_nomes)):
                print("Nome Excluído com sucesso! ")
            else:
                print("O nome não existe na lista...")
        elif opcao == '0':
            print("###### Encerrando o programa...")
            break
        else:
            print("----- Você não digitou uma opção do menu, por favor, digite novamente! ")

main()
