maior = 0
menor = 0
for p in range(1, 4):
    peso = float(input(f'Qual o Peso da {p}º pessoa? '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior: # aqui é o maior
            maior = peso

        if peso < menor: # aqui é o menor
            menor = peso

print('O maior peso lido foi: {}Kg'.format(maior))
print('O menor peso lido foi: {}Kg'.format(menor))