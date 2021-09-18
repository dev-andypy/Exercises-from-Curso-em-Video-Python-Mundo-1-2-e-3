lista = []
lista2 = []
cont = ''
while True:
    n = int(input('Digite um Valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor Adicionado com Sucesso...')
    else:
        print('Valor duplicado!! Não vou adicionar...')
        lista2.append(n)
    cont = str(input('Deseja continuar? [S/N] '))
    if cont in 'Nn':
        break
print('=-'*30)
print(f'Voce digitou os valores {sorted(lista)}')
print(f'E por conta de ser duplicado deixou de adicionar {sorted(lista2)}')