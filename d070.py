totC = maior = barato = cont = 0
nmenor = ' '
print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)
while True:
    produto = str(input('Digite o Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    resp = ' '
    totC += preço
    if preço > 1000:
        maior += 1
    elif  cont == 1 or preço < barato:
        barato = preço
        nmenor = produto
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N] '))
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'o total da compra foi {totC:.2f}')
print(f'temos {maior} produto(s) maior que R$1000')
print(f'O produto mais barato foi {nmenor} e custou R${barato:.2f}')