def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! por favor, digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[1;31mEntradas de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n
def LeiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! por favor, digite um número real válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[1;31mEntradas de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n


n1 = LeiaInt('Digite um número inteiro: ')
n2 = LeiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n1}.')
print(f'O valor real digitado foi {n2}.')