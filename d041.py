from datetime import date
nasc = int(input('Digite Seu ano de Nascimento: '))
atual = date.today().year
idade = atual - nasc
print('Você nasceu em {} e tem {} portanto:'.format(nasc, idade))
if idade <= 9:
    print('Já que você tem {} anos você é um atleta MIRIM'.format(idade))
elif idade <= 14:
    print('Já que você tem {} anos você é um atleta INFANTIL'.format(idade))
elif idade <= 19:
    print('Já que você tem {} anos você é um atleta JÚNIOR'.format(idade))
elif idade <=25:
    print('Já que você tem {} anos você é um atleta SÊNIOR'.format(idade))
elif idade > 25:
    print('Já que você tem {} anos você é um atleta MASTER'.format(idade))
