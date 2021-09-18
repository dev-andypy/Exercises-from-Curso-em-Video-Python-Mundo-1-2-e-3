cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'desesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while 0 <= num <= 20:
        print('Tente Novamente. ', end='')
    print(f'Você digitou o número {cont[num]}')
    continuar = str(input('Você quer continuar?[S/N] ')
    if continuar in 'Nn' :
        break
print('FIM DO PROGRAMA')



