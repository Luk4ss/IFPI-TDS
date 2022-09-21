"""8) Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes
ocorreu a letra ‘A’."""


def conta_ocorrencia_letra_A(lista):
    count = 0
    for ltr in lista:
        if ltr == 'A':
            count += 1
    return count


def main():
    lista_de_letras = []
    while True:
        letra = input("Digite uma letra do alfabeto ou aperte '*' para sair: ").upper()
        if  letra >= "A" and letra <= "Z" and len(letra) == 1:
            lista_de_letras.append(letra)
        elif letra == '*':
            break
        elif len(letra) > 1:
            print('Você digitou mais do que um caractere...')
        else:
            print('\nVocê não digitou uma letra do alfabeto...\n')
    
    qtd_letraA = conta_ocorrencia_letra_A(lista_de_letras)
    if qtd_letraA == 0:
        print("\nA lista não possui a letra A")
    else:
        print(f"\nA letra A aparece {qtd_letraA} veze(s) na lista")
   
        
main()
