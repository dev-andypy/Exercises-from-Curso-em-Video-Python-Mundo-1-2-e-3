palavras = ('curso', 'Boia', 'astuto', 'lixo', 'louco', 'amar', 'odiar',
            'bote', 'programacao', 'python', 'video', 'gratuito', 'lembrança',
            'dificuldade', 'vida', 'conjunto')
for p in palavras:
    print(f'\n Na palavra {p.upper()} Temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
