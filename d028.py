import random
n = random.randint(0, 5)
user = int(input('Digite Um número entre 0 e 5: '))
if user == n:
    print('O Computador Pensou a mesma coisa! PARABÉNS!')
else:
    print('O Computador pensou no número {}, foi mal tenta de novo!'.format(n))