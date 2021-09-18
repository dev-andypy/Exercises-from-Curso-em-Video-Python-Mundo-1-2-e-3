time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas Partidas {jogador["Nome"]} Jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'     Quantos Gols {jogador["Nome"]} fez na partida {c + 1}: ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas) #o comando "sum()" faz a soma do item inserido dentro
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar?[S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N')
    if resp == 'N':
        break
print('-'*40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    busca = int(input('Mostrar dados de qual jogador?(999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO não existe jogador com o código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}: -- ')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-'*40)
print('<<< Volte Sempre >>>')