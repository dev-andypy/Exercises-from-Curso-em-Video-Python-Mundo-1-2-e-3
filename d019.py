import random
aluno1 = str(input('Digite o nome Primeiro Aluno: '))
aluno2 = str(input('Digite o nome Segundo Aluno: '))
aluno3 = str(input('Digite o nome Terceiro Aluno: '))
aluno4 = str(input('Digite o nome Quarto Aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print('O(a) Aluno(a) escolhido(a) foi {}'.format(escolhido))