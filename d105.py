def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param num: uma ou mais notas dos alunos
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    ficha = dict()
    ficha['Total'] = len(num)
    ficha['Maior'] = max(num)
    ficha['Menor'] = min(num)
    ficha['Média'] = sum(num)/len(num)
    if sit:
        if ficha['Média'] >= 7:
            ficha['Situação'] = 'BOA'
        elif ficha['Média'] >= 5:
            ficha['Situação'] = 'RAZOÁVEL'
        else:
            ficha['Situação'] = 'RUIM'
    return ficha


resp = notas(5.5, 2.5, 10, sit = True)
print(resp)
help(notas)