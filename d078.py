listanum = []
mai = men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite o valor para posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if mai < listanum[c]:
            mai = listanum[c]
        if men > listanum[c]:
            men = listanum[c]

print('=-'*30)
print(f'Digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} na(s) posição(ões): ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end=' ')
print()
print(f'O menor valor digitado foi {men} na(s) posição(ões): ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end=' ')
print()
