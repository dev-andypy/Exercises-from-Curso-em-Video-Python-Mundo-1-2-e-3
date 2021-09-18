peso = float(input('Qual é o seu Peso? (Kg) '))
altura = float(input('Qual sua Altura? (m) '))
imc = peso / altura ** 2
print(
    'Ja que seu peso é {:.2f}Kg e sua altura {:.2f}m seu IMC é {:.2f} o que te leva a ser De Acordo com seu '
    'índice:'.format(
        peso, altura, imc))
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc <= 25:
    print('PESO IDEAL')
elif imc <= 30:
    print('SOBREPESO')
elif imc <= 40:
    print('OBESO')
else:
    print('OBESIDADE MÓRBIDA')
