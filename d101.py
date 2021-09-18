def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
                    #JEITO DO GUANABARA
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'

                    #SEU JEITO
    #if idade < 18:
     #   if idade < 18 and idade >= 16:
      #      print(f'Com {idade} anos: VOTO OPCIONAL!')
       # else:
        #    print(f'Com {idade} anos: NÃO VOTA!')
    #else:
     #   if idade >= 70:
      #      print(f'Com {idade} anos: VOTO OPCIONAL!')
       # else:
        #    print(f'Com {idade} anos: VOTO OBRIGATÓRIO!')'''


print('-'*30)
nasc = int(input('Digite o ano que você nasceu: '))
print(voto(nasc))