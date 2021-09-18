num = int(input('Digite um número inteiro: '))
print('-=-'*15)
print('''Escolha uma das bases para conversão:
[ 1 ]Converter Para BINÁRIO
[ 2 ]Converter Para OCTAL
[ 3 ]Converter Para HEXADECIMAL''')
print('-=-'*15)
opcao = int(input('Sua Opção: '))
print('-=-'*15)
if opcao == 1:
    print('Em BINÁRIO o número {} fica {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('Em OCTAL o número {} fica {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('Em HEXADECIMAL o número {} fica {}'.format(num, hex(num)[2:]))
else:
    print('Opção INVÁLIDA, Tente Novamente')
print('-=-' * 15)