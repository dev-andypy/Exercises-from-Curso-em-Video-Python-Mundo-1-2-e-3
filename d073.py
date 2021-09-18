times = ('Bragantino', 'Atlético-PR', 'Palmeiras', 'Fortaleza', 'Bahia',
         'Santos', 'Atlético-GO', 'Atlético-MG', 'Fluminense', 'Flamengo', 'Corinthians',
         'Ceará SC', 'Internacional', 'Juventude','Sport Recife','Cuiabá', 'São Paulo', 'Chapecoense',
         'América-MG','Grêmio')
print(f'os Times do Brasileirão: {times}')
print('='*30)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('='*30)
print(f'Os ultimos 4 Colocas: {times[-4:]}')
print('='*30)
print(f'Times em ordem Alfabética: {sorted(times)}')
print('='*30)
print(f'O time Chapecoense está na posição: {times.index("Chapecoense")+1}ª')