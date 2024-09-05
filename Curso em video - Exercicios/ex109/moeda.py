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
