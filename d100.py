from random import randint
from time import sleep
def sortear(numeros):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!', end='')
    print()
def somapar(numeros):
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

lista = list()
sortear(lista)
somapar(lista)