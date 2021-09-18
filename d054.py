from datetime import date
count = 0
count2 = 0
data = date.today().year
for ano in range(1, 8):
    nascimento = int(input('Em que ano a {}º pessoa nasceu? '.format(ano)))
    idade = data - nascimento
    if idade >= 18:
        count += 1
    elif idade < 18:
        count2 += 1
print('=-='*12)
print('Ao Todo tivemos {} pessoas maiores de idade'.format(count))
print('E Também {} pessoas menores de idade'.format(count2))
print('=-='*12)