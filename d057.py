sexo = str(input('Informe seu sexo:[M/F] ')).strip().upper()[0]
while sexo not in 'MmFf': #Traduzindo: enquanto o sexo não estiver entre essas palavras, 'MmFf' execute:
    sexo = str(input('Dados inválidos, por favor insira seu Sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
