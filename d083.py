expr = str(input('Digite a expressão: '))
pilha: []
for símb in expr:
    if símb == '(': #Cada vez que tiver um parêntese aberto ele coloca um parêntese aberto na pilha
        pilha.append('(')
    elif símb == ')': #
        if len(pilha) > 0:#para verificar se ele não está vazio
            pilha.pop()
        else:#Se ela não tiver vazia é um sinal QUE TEVE MAIS PARÊNTESES DOQ O NECESSÂRIO
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua Expressão está inválida')

