from datetime import date
ano = int(input('Qual o ano que deseja analisar? Coloque 0 se quiser analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0:
    print('O ano de {} É Bissexto!'.format(ano))
else:
    print('O Ano de {} NÃO é Bissexto'.format(ano))