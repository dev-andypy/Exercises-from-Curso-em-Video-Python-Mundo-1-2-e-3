import math
ang = float(input('Digite o Angulo desejado: '))
print('Com o Valor do Ângulo sendo {:.2f}, O Valor de Seno é {:.2f}'.format(ang, math.sin(math.radians(ang))))
print('Com o Valor do Ângulo sendo {:.2f}, O Valor do Cosseno é {:.2f}'.format(ang, math.cos(math.radians(ang))))
print('Com o Valor do Ângulo sendo {:.2f}, O Valor da Tangente é {:.2f}'.format(ang, math.tan(math.radians(ang))))