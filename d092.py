from datetime import datetime
ficha = dict()
ficha['Nome'] = str(input('Nome: '))
ficha['Idade'] = int(input('Ano de Nascimento: '))
ficha['Idade'] = datetime.now().year - ficha['Idade']
ficha['CTPS'] = int(input('Carteira de Trabalho (0 caso não tenha): '))
if ficha['CTPS'] != 0 :
    ficha['Contratação'] = int(input('Ano de Contratação: '))
    ficha['Salário'] = float(input('Salário: R$'))
    ficha['aposentadoria'] = ficha['Idade'] + ((ficha['Contratação'] + 35) - datetime.now().year)
print('-='*30)
for k, v in ficha.items():
    print(f'    - {k} tem o valor {v}')