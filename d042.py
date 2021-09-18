print('-=-'*12)
print('Analisador de Triângulos V2.0')
print('-=-'*12)
r1 = float(input('Digite o Primeiro Segmento: '))
print('_'*12)
r2 = float(input('Digite o Segundo Segmento: '))
print('_'*12)
r3 = float(input('Digite o Terceiro Segmento: '))
print('-_-'*12)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmentos acima PODEM FORMAR UM TRIÂNGULO!')
    print('-_-'*12)
    if r1 == r2 == r3:
        print('É EQUILÁTERO já que todos os lados são iguais')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r1 == r3 != r2:
        print('É ISÓSCELES já que 2 são iguais e 1 é diferente')
    elif r1 != r2 != r3 != r1:
        print('É ESCALENO já que todos os lados são diferentes')
else:
    print('Os Segmentos Acima NÃO PODEM FORMAR UM TRIÂNGULO')
print()
print('-=-'*6, 'FIM', '-=-'*6)