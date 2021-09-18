frase = str(input('Digite uma Frase: ')).strip().upper()
junto = frase.replace(' ', '')
inverso = ''
# inverso = junto[::-1] (uma maneira mais fácil de inverter)
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('A frase "{}" invertida fica "{}"'.format(frase, inverso))
if inverso == junto:
    print('Essa Frase é um Palíndromo!')
else:
    print('Essa Frase não é um Palíndromo')
