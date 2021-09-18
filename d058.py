from random import randint
#primeiro passo criar as variáveis e o contador
computador = randint(0, 10)
jogador = ''
palpites = 0 #contador
print('''Sou seu computador...
Acabei em pensar em um número de 0 a 10.
Consegue adivinhar qual foi??''')
print('-=-'*12)
while jogador != computador: #Enquanto Jogador for diferente de computador execute:
    jogador = int(input('Qual seu Palpite? '))
    if jogador != computador and jogador < computador:
        print('Mais... tente novamente.')
    elif jogador != computador and jogador > computador:
        print('Menos... Tente novamente')
    palpites += 1
print('-=-'*12)
print('Você acertou com {} tentativas. PARABÉNS!!'.format(palpites))