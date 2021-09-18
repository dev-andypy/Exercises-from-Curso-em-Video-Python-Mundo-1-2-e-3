casa = float(input('Digite o Valor da casa: R$'))
salario = float(input('Digite o Valor do Salário: R$'))
anos = int(input('Em quantos anos você vai pagar? '))
print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f}'.format(casa, anos, casa/(anos*12)))
print('=-='*15)
if casa/(anos*12) > salario*30/100:
    print('EMPRÉSTIMO NEGADO!')
else:
    print('EMPRÉSTIMO ACEITO!')
print('=-='*15)