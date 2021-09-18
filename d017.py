import math
co = float(input('Digite o Valor do Cateto Oposto: '))
cads = float(input('Digite o Valor do Cateto Adjascente: '))
cal = math.hypot(co, cads)
print('Com o Cateto Oposto sendo {:.2f} e o Adjascente sendo {:.2f}, a hipotenusa é {:.2f}'.format(co, cads, cal ))