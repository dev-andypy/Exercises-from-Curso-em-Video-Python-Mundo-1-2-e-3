n = int(input('Digite um Número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! :'.format(n))
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('O fatorial de {} é {}'.format(n, f))