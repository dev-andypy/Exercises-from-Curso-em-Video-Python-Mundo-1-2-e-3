sal = float(input('Digite o Valor do Salário do Funcionário: R$'))
novo = sal + (sal*15/100)
print('Seu salário inicial era R${:.2f}, porém com o reajuste de +15% seu salário atual é R${:.2f}'.format(sal, novo))