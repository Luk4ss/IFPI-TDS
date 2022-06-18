
def celsiusToKelvin(Tc):
    Tk = Tc + 273.15
    temperature_kelvin.append(Tk.__round__(2))


def fahrenheitToKelvin(Tf):
    Tk = (5 * (Tf - 32) / 9) + 273.15
    temperature_kelvin.append(Tk.__round__(2))


meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro')

temperature_kelvin = []

for _ in range(12):
    temp = float(input().strip())
    escale = input().strip()
    if escale.upper() == 'K':
        temperature_kelvin.append(temp)
    elif escale.upper() == 'C':
        celsiusToKelvin(temp)
    elif escale.upper() == 'F':
        fahrenheitToKelvin(temp)


temperatura_media = sum(temperature_kelvin)/(len(temperature_kelvin))

print("TEMPERATURA MÉDIA ANUAL")
print(f'{temperatura_media.__round__(2)}K')
print("TEMPERATURAS ACIMA DA MÉDIA ANUAL:")
for temp in temperature_kelvin:
    if temp > temperatura_media:
        pos = temperature_kelvin.index(temp)
        print(f'{meses[pos]}: {temp}K')
