nome = str(input('Digite seu nome completo: ')).strip()
print('Seu Primeiro nome É: {}'.format(nome.split()[0]))
print('Seu Ultimo nome É: {}'.format(nome[len(nome)-1]))