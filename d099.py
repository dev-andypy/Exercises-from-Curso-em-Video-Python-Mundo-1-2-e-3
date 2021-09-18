from time import sleep
def maior(*num):
    print('-=' * 20)
    print('Analisando os valores passados...')
    cont = m = 0
    for n in num:
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            m = n
        else:
            if n > m:
                m = n
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {m}')



maior(5, 7, 8, 4, 23)
maior(5,6,8)
maior(1, 2)
maior(6)
maior()
