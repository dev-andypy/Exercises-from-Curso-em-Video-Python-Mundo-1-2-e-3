print('-=-'*6,'Tabuada V2.0','-=-'*6)
tabuada = int(input('Digite o Número da Tabuada que você deseja ver: '))
print('-=-'*16)
for t in range(0, 11):
    print('{} x {} = {}'.format(tabuada, t, tabuada*t))
print('-=-'*6, 'FIM', '-=-'*6)