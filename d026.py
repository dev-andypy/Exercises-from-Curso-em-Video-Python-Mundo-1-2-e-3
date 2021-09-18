frase = str(input('Digite uma frase: ')).lower()

print('A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('-'*12)
print('ela aparece pela primeira vez no bloco {}'.format(frase.find('a')))
print('-'*12)
print('e na ultima vez ela reaparece no bloco {}'.format(frase.rfind('a')+1))