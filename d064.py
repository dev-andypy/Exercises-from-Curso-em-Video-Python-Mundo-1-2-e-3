n = count = soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    count += 1
    if n != 999:
        soma += n

print('Você Digitou {} números e a soma entre eles foi de {}'.format(count, soma))


