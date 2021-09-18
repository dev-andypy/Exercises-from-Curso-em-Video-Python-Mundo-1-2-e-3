print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Digite o Primeiro Segmento: '))
r2 = float(input('Digite o Segundo Segmento: '))
r3 = float(input('Digite o Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmentos acima PODEM FORMAR UM TRIÂNGULO!')
else:
    print('Os Segmentos Acima NÃO PODEM FORMAR UM TRIÂNGULO')