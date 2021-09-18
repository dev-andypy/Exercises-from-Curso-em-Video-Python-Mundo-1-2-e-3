matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somacol = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        #if c == 2: #o jeito antigo de encontrar a soma dos valores da ultima coluna
            #somacol += matriz[l][c]
       # if l == 1: #o jeito padrão que se usaria para encontrar o maior valor da ultima coluna
        #    if c == 0:
          #      maior = matriz[l][c]
         #   else:
          #      if matriz[l][c] > maior:
           #         maior = matriz[l][c]

print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*30)
print(f'A soma dos valores pares é {somapar}.')
for l in range(0, 3): #um jeito diferente de encontrar a soma dos valores da ultima coluna
    somacol += matriz[l][2]
print(f'A soma dos valores da última coluna é {somacol}.')
for c in range(0, 3): #Um jeito diferente de achar o maior valor da segunda linha
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
print(f'o maior valor da segunda linha é {maior}.')
