from time import sleep
val1 = int(input('Digite o Primeiro valor: '))
val2 = int(input('Digite o Segundo valor: '))
opção = 0
while opção != 5:
    print('''
    [ 1 ] Soma
    [ 2 ] Multiplicação
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] sair o programa''')
    opção = int(input('>>>>Qual sua opção? '))
    print('-=-'*12)
    if opção == 1:
        print('a soma entre {} + {} é {}'.format(val1, val2, val1 + val2))
    elif opção == 2:
        print('A multiplicação entre {} x {} é {}'.format(val1, val2, val1*val2))
    elif opção == 3:
        print('Entre {} e {} o maior número é {}'.format(val1, val2,max(val1, val2)))
    elif opção == 4:
        val1 = int(input('Digite o Primeiro novo número: '))
        val2 = int(input('Digite o Segundo novo número: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida, Tente de Novo')
    sleep(2)
print('FIM')
print('-=-'*12)
