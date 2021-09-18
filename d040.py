nota1 = float(input('Digite a Primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if media < 5.0:
    print('O Aluno está REPROVADO')
elif media >= 5.0 and media < 7.0:
    print('O Aluno está de RECUPERAÇÃO')
else:
    print('O Aluno está APROVADO')