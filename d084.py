pessoas = list()
dado = list()
pesmai = pesmen = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(pessoas) == 0:#Se não foi cadastrado ninguém execute:
        pesmai = pesmen = dado[1]
    else:
        if dado[1] > pesmai:
            pesmai = dado[1]
        if dado[1] < pesmen:
            pesmen = dado[1]

    pessoas.append(dado[:])
    dado.clear()
    resp = str(input('Quer Continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'ao todo voce cadastrou {len(pessoas)} pessoas')
print(f'O maior peso registrado foi {pesmai}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == pesmai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso registrado foi {pesmen}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == pesmen:
        print(f'[{p[0]}]', end='')
print()