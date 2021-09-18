ficha = dict()
ficha['Nome'] = str(input('Nome: '))
ficha['Média'] = float(input(f'Média de {ficha["Nome"]}: '))
if ficha['Média'] >= 7:
    ficha['Situação'] = 'APROVADO'
elif ficha['Média'] < 7 and ficha['Média'] >= 5:
    ficha['Situação'] = 'Recuperação'
else:
    ficha['Situação'] = 'REPROVADO'
print('-='*30)
for k, v in ficha.items():
    print(f'- {k} é igual a {v} ')


