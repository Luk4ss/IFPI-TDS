def gravar_lista(lista):
    for i in range(10):
      num = int(input(f'Digite o elemento {i+1}: '))
      lista.append(num)

def intercalar_lista(l1, l2):
    l3 = []
    for i in range(10):
       l3.append(l1[i])
       l3.append(l2[i])
    return l3


def intercalar_lista_2(l1, l2):
    l3 = [0]*20
    index_lista1 = 0
    index_lista2 = 0
    for i in range(20):
       if i % 2 == 0:
         l3[i] = l1[index_lista1]
         index_lista1 += 1
       else:
          l3[i] = l2[index_lista2]
          index_lista2 += 1

    return l3


def main():
   while True:
       try:
          lista1 = []
          lista2 = []
          gravar_lista(lista1)
          print("---------------")
          gravar_lista(lista2)
          print("---------------")
          lista3 = intercalar_lista(lista1, lista2)
          print("---------------")
          lista4 = intercalar_lista_2(lista1, lista2)
          print(lista3)
          print("---------------")
          print(lista4)
          break
       except:
          print('--- Você digitou um dado inválido ----\n')


main()
