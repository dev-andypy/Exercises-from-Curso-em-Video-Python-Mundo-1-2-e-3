from time import sleep
def contador(a, b, c):
    print('-=' * 20)
    print(f'Contagem de {a} até {b} de {c} em {c}:')
    sleep(2.5)
    if c > 0:
        for c in range(a, b + 1, c):
            print(f'{c}', end =' ', flush=True)
            sleep(0.5)
        print('FIM!', end='',flush=True)
        print()
    elif c < 0:
        for c in range(a, b - 1, c):
            print(f'{c}', end =' ', flush=True)
            sleep(0.5)
        print('FIM!', end='',flush=True)
        print()


contador(1, 10, 1)
contador(10, 0, -2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)

