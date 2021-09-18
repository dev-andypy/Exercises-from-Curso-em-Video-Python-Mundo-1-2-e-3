a = int(input('Digite o Primeiro valor: '))
b = int(input('Digite o Segundo valor: '))
c = int(input('Digite o Terceiro valor: '))
#Verificando quem é o menor
menor = a
if b<c and b<a:
    menor = b
if c<a and c<b:
    menor = c
#Verificando quem é o maior
maior = a
if b>c and b>a:
    maior = b
if c>a and c>b:
    maior = c
print('o menor valor digitado foi {}'.format(menor))
print('o maior valor digitado foi {}'.format(maior))