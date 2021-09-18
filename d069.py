maior = homem = mulher = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-'*20)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if idade > 18:
        maior += 1
    elif sexo in 'M':
        homem += 1
    elif sexo in 'F' and idade < 20:
        mulher += 1
    elif continuar in 'N':
        break
print(f'''Total de pessoas com mais de 18: {maior};

Total de homens cadastrados: {homem};

Total de mulheres com menos de 20 anos: {mulher}.''')
    