def fatorial(num, show=False):
    
    print('-' * 30)
    f = 1
    for n in range(num, 0, -1):
        if show:
            print(n, end=' ')
            if n > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= n
    return f
    #print(f'{f}', end='')
    #print()


# Programa Principal
print(fatorial(5, show=True))
