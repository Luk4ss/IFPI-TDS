alfabeto = "abcdefghijklmnopqrstuvwxyz"

chave = int(input("Digite a sua chave: "))

letra = input("Por favor, entre com uma letra para criptografar: ")[0]

posicao = alfabeto.find(letra)

nova_posicao = (posicao + chave) % 26

letra_criptografada = alfabeto[nova_posicao]

print("Sua letra criptografada é : " + letra_criptografada)


# Descriptografia

chave_d = int(input("Digite a sua chave de descriptografia: "))
letra_c = input("Por favor, entre com uma letra para descriptografar: ")[0]

posicao = alfabeto.find(letra_c)

nova_posicao = (posicao - chave_d) % 26

letra_descriptografada = alfabeto[nova_posicao]

print("Sua letra criptografada é : " + letra_descriptografada)
