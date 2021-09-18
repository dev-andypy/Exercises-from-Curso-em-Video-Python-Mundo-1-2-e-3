print('='*15)
print('10 TERMOS DE UMA PA')
print('='*15)
pt = int(input('Digite o Primeiro Termo: '))
r = int(input('Digite a Razão: '))
décimo = pt + (10 - 1) * r
for c in range(pt, décimo + r, r):
    print('{} '.format(c), end='--> ')
print('ACABOU')