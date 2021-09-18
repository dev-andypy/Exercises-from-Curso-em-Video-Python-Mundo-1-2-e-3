import moeda
val = float(input('Digite o valor da compra: R$'))
print(f'A metade de {val} é {moeda.metade(val)}')
print(f'O dobro de {val} é {moeda.dobro(val)}')
print(f'aumentando 10%, temos {moeda.aumentar(val, 10)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(val, 13)}')