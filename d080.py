lista = []
for c in lista:
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]: #se for o primeiro valor ou o número for maior que o ultimo valor da lista execute
        lista.append(n)
        print('Valor adcionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista): #enquanto a posição for menor q o tamanho da lista execute
            if n <= lista[pos]: #Se o número digitado for menor ou igual a posição atual da lista execute
                lista.insert(pos, n)
                print(f'Valor adcionado na posição {pos} da lista...')
                break
            pos += 1
print('-='*30)
print(f'Os Valores digitados em ordem foram {lista}')