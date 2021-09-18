distancia = float(input('Digite a distância da viagem: '))
print('-=-'*30)
if distancia <= 200:
    print('Ja que a viagem tem até 200Km de distância o preço da Viagem é de R${:.2f}'.format(distancia*0.50))
else:
    print('Pela Viagem ser mais longa o preço acaba sendo de R${}'.format(distancia*0.45))
print('-=-'*30)
print('Tenha uma ótima viagem!')
