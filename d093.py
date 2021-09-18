dados = dict()
goleadas = list()
dados['Nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas Partidas {dados["Nome"]} Jogou? '))
for c in range(0, tot):
    goleadas.append(int(input(f'     Quantos Gols {dados["Nome"]} fez na partida {c + 1}: ')))
dados['Gols'] = goleadas[:]
dados['Total'] = sum(goleadas) #o comando "sum()" faz a soma do item inserido dentro
print('-='*30)
print(dados)
print('-='*30)
for k,v in dados.items():
    print(f'O campo {k} tem o valor {v}...')
print('-='*30)
print(f'O Jogador {dados["Nome"]} Jogou {tot}')
for i, v in enumerate(goleadas):
    print(f'    => Na partida {i + 1}, fez {v}')
print(f'Foi um total de {dados["Total"]} gols.')