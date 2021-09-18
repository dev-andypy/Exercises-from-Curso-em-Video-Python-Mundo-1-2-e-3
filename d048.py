soma = 0 #criou um acumulador
cont = 0 #criou um contador
for n in range(1, 501, 2):# Normalmente o acumulador soma um valor e o contador soma 1
    if n % 3 == 0:
        cont = cont + 1
        soma = soma + n #fez com que a soma recebesse o que ela tem + o número, ou seja, está acumulando o número
print('A soma de todos os {} números é {}'.format(cont, soma))