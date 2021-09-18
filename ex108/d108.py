from ex108 import moeda
val = float(input('Digite o valor da compra: R$'))
print(f'A metade de {moeda.moeda(val)} é {moeda.moeda(moeda.metade(val))}')
print(f'O dobro de {moeda.moeda(val)} é {moeda.moeda(moeda.dobro(val))}')
print(f'aumentando 10%, temos {moeda.moeda(moeda.aumentar(val, 10))}')
print(f'Diminuindo 13%, temos {moeda.moeda(moeda.diminuir(val, 13))}')