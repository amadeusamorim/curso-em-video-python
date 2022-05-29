def aumentar(preço=0, taxa=0, form=False):
    res = preço + (preço * (taxa/100))
    return res if form is False else moeda(res)


def diminuir(preço=0, taxa=0, form=False):
    res = preço - (preço * (taxa/100))
    return res if form is False else moeda(res)


def dobro(preço=0, form=False):
    res = preço * 2
    return res if not form else moeda(res)


def metade(preço=0, form=False):
    res = preço / 2
    return res if not form else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def resumo(preço=0, taxaa=0, taxad=0, form=True):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    aum = preço - (preço * (taxaaum / 100))
    dim = preço - (preço * (taxadim / 100))
    dob = preço * 2
    div = preço / 2
