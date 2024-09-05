def moeda(txt):
    res = 'R$' + str(txt).replace('.', ',')
    return res


def dobro(num=0, formato=False):
    res = num*2
    return res if formato is False else moeda(res)


def metade(num=0, formato=False):
    res = num*2
    return res if formato is False else moeda(res)


def aumentar(num=0, taxa=0, formato=False):
    res = num+(num*taxa/100)
    return res if formato is False else moeda(res)


def diminuir(num=0, taxa=0, formato=False):
    res = num+(num*taxa/100)
    return res if formato is False else moeda(res)


def resumo(num:float=0, taxaA=0, taxaD=0, formato=True):
    print('--'*20)
    print(f'{"RESUMO DO VALOR":^40}')
    print('--'*20)
    print(f'Preço analisado:\t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num,formato)}')
    print(f'Metade do preço:\t{metade(num,formato)}')
    print(f'{taxaA}% de aumento: \t{aumentar(num,taxaA,formato)}')
    print(f'{taxaD}% de redução: \t{diminuir(num,taxaD,formato)}')
    print('--'*20)
