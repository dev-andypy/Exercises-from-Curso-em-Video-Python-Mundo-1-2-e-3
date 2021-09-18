lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar:[S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'foi digitado {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os Valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O Valor 5 Faz parte da lista')
else:
    print('O valor 5 Não foi encontrado na lista')