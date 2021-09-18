nome = str(input('Digite seu Nome: ')).strip()
dividido = nome.split()

print('Seu nome com todas as letras maiúsculas fica assim: {}'.format(nome.upper()))

print('Seu nome com todas as letras minúsculas fica assim: {}'.format(nome.lower()))

print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))

print('Seu Primeiro Nome tem {} letras'.format(len(dividido[0])))