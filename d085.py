valor = 0
num = [[], []]

for c in range(0, 8):
    valor=int(input(f'digite o {c}º.Valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    elif valor % 2 == 1:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares são: {num[0]}')
print(f'Os valores impares são: {num[1]}')

