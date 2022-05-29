def notas(*nota, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param nota: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dados = dict()
    dados["total"] = len(nota)
    dados["maior"] = max(nota)
    dados["menor"] = min(nota)
    dados["media"] = sum(nota)/len(nota)
    if sit:
        if dados["media"] >= 7:
            dados["situação"] = 'BOA'
        elif dados["media"] >= 5:
            dados["situação"] = 'RAZOÁVEL'
        else:
            dados["situação"] = 'RUIM'
    return dados


resp = notas(5.5, 2.5, 9, 8.5, 6, 9.2, sit=True)
print(resp)
