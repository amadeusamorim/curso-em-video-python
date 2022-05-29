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
    print('-' * 30)
    print(f'{"RESUMO DO VALOR".center(30)}')
    print('-' * 30)
    print(f"Preço analisado: \t{moeda(preço)}")
    print(f"Dobro do preço: \t{dobro(preço, True)}")
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxad}% de redução: \t{diminuir(preço, taxad, True)}')
    print('-' * 30)