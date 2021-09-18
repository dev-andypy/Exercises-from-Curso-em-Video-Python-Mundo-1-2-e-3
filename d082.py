lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar: [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        if v % 2 != 0:
            impares.append(v)
print('-='*30)
print(f'A Lista completa é {lista}')
print(f'A lista de número pares é {pares}')
print(f'A lista de número impares é {impares}')

