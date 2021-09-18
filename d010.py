larg = float(input('Digite a Largura da sua Parede: '))
alt = float(input('Digite a Altura da sua Parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é {}m².'.format(larg, alt, area))
tinta = area / 2
print('para pintar essa parede você precisará de {}l de tinta.'.format(tinta))