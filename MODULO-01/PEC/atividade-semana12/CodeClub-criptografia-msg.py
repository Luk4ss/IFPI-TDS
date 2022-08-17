def cryptMessage(key, msg):
    message = ""
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    for letra in msg:
        posicao = alfabeto.find(letra)
        nova_posicao = (posicao + key) % 26
        message += alfabeto[nova_posicao]

    return message


chave = int(input("Digite a sua chave: "))

mensagem = input("Por favor, entre com uma mensagem para criptografar: ")

print("Sua mensagem criptografada é: " + cryptMessage(chave, mensagem))

# Descriptografia

chave = int(input("Digite a sua chave de descriptografia: "))
mensagem = input("Por favor, entre com a mensagem que deseja descriptografar: ")

print("Sua mensagem descriptografada é: " + cryptMessage(-chave, mensagem))
