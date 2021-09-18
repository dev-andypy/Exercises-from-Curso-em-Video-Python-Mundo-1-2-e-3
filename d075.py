nums = (int(input('Digite o primeiro número: ')),
        int(input('Digite o Segundo número: ')),
        int(input('Digite o Terceiro número: ')),
        int(input('Digite o último número: ')),)
print(f'Você digitou os valores {nums}')
print(f'o valor 9 apareceu {nums.count(9)} vezes')
if 3 in nums:
    print(f'O Valor 3 apareceu na {nums.index(3) + 1}ª posição')  # o ".index" mostra a posição do valor desejado
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os Números pares digitados foram ', end='')
for n in nums:
    if n % 2 == 0:
        print(n, end=' ')
