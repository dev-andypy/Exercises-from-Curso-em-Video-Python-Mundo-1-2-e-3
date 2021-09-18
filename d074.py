from random import randint
maior = menor = cont = 0
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ')
for n in numeros:
    print(f'{n} ', end='')
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'\nmaior = {maior}')
print(f'menor = {menor}')
#print(f'menor = {min(numeros)}")
#print(f'maior = {max(numeros)}") #uma outra forma de achar o maior e menor valor

