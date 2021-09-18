print('Gerador de PA!')
print('-=' * 10)
primeiro = int(input('Digite o Primeiro Termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    while cont <= total:
        total += mais
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer ver a mais? '))
print('Progressão finalizada com {} termos utilizado'.format(total))
