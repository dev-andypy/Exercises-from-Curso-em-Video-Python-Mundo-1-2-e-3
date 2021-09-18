v = float(input('Qual a velocidade do carro? '))
if v > 80 :
    print('MULTADO! Você excedeu o limite de 80Km/h')
    multa = (v-80) * 7
    print('Você deve pagar a multa de R${:.2f}'.format(multa))
print('Tenha um Bom dia e dirija com segurança')