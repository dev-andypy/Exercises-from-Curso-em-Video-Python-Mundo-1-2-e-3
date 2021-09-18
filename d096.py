def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg:.1f}X{comp:.1f} é de {a:.1f}m²')


print('Controle de Terrenos')
print('-'*15)
l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))
area(l, c)