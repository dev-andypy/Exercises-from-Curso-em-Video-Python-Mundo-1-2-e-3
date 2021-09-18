from ex109 import moeda
val = float(input('Digite o valor da compra: R$'))
print(f'A metade de {moeda.moeda(val)} é {moeda.metade(val, True)}')
print(f'O dobro de {moeda.moeda(val)} é {moeda.dobro(val, True)}')
print(f'aumentando 10%, temos {moeda.aumentar(val, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(val, 13, True)}')