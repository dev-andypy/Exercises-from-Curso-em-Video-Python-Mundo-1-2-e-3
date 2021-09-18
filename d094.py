pessoas = list()
ficha = dict()
soma = 0
while True:
    ficha['Nome'] = str(input('Nome: '))
    ficha['Sexo'] = str(input('Sexo M/F: '))[0]
    if ficha['Sexo'] not in 'MmFf':
        while ficha['Sexo'] not in 'MmFf':
            print('ERRO! Responda apenas com M ou F')
            ficha['Sexo'] = str(input('Sexo M/F: '))[0]
    ficha['Idade'] =  int(input('Idade: '))
    soma += ficha['Idade']
    pessoas.append(ficha.copy())
    resp = str(input('Quer Continuar?[S/N] '))[0]
    if resp not in 'SsNn':
        while resp not in 'SsNn':
            print('ERRO! Responda apenas com S ou N')
            resp = str(input('Quer Continuar?[S/N] '))[0]
    if resp in 'Nn':
        break
print('-='*30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
media = soma / len(pessoas)
print(f'B) A média de idade é de {media} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]}; ', end='')
print()
print('D) Lista de pessoas acima da média: ', end='')
for p in pessoas:
    if p['Idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<ENCERRADO>>')
