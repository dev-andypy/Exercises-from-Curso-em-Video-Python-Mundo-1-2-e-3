num1 = int(input('Digite o Primeiro Número: '))
print('-_-'*20)
num2 = int(input('Digite o Segundo Número: '))
print('-_-'*20)
if num1 > num2:
    print('O PRIMEIRO Número é maior')
elif num2 > num1:
    print('O SEGUNDO Número é maior')
elif num1 == num2 and num2 == num1:
    print('Os Dois Número são IGUAIS')
print('-_-'*20)