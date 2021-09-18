d = int(input('Quantos dias fazem que o carro foi alugado? '))
km = float(input('Quantos Quilômetros o carro rodou? '))
print('Ja que o carro foi alugado {} dias atrás e rodou {}Km, O total a pagar será R${}.'.format(d, km, (d*60)+(km*0.15)))