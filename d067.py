n = 0
while True:
    n = int(input('Digite a Tabuada que deseja ver: '))
    if n < 0:
        break
    print('-'*30)
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')
    print('-'*30)

print('Programa TABUADA ENCERRADO!!')