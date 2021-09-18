soma = count = 0
while True:
    valor = int(input('Digite um número[999 para parar]: '))
    count += 1
    if valor == 999:
        break
    soma += valor
print(f'Você digitou {count} números e a soma entre eles foi igual a {soma}')