salario = float(input('Digite seu salário: '))
if salario > 1250:
    print('Pelo seu sálario de {} ser acima de R$1250.00 então agora ele vale R${:.2f}'.format(salario, salario+(salario*10/100)))
else:
    print('Ja que seu salário de {} é abaixo de R$1250.00 ele agora custará R${}'.format(salario, salario+(salario*15/100)))