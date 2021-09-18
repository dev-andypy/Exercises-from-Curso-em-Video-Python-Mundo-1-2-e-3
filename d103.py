def ficha(nome='<Desconhecido>', gol=0):
    print(f'o Jogador {nome} fez {gol} gol(s) no campeonato')

n = str(input('Digite o nome do Jogador: '))
g = str(input('Digite a quantidade de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
