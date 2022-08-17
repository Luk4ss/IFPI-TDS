vogais = {}
texto = input().strip()

count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

for letra in texto:
    if letra == 'a' or letra == 'à' or letra == 'â' or letra == 'ã' or letra == 'á' or letra == 'A' or letra == 'Á':
        count_a += 1

    elif letra == 'e' or letra == 'é' or letra == 'ê' or letra == 'E':
        count_e += 1

    elif letra == 'i' or letra == 'í' or letra == 'I':
        count_i += 1

    elif letra == 'o' or letra == 'ó' or letra == 'ô' or letra == 'O':
        count_o += 1

    elif letra == 'u' or letra == '' or letra == 'ú' or letra == 'U':
        count_u += 1

vogais['A'] = count_a
vogais['E'] = count_e
vogais['I'] = count_i
vogais['O'] = count_o
vogais['U'] = count_u

for vogal in vogais:
    print(f'{vogal}: {vogais[vogal]}')
