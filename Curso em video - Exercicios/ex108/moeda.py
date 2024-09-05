def moeda(valor):
    valor = 'R$' + str(f'{valor:.2f}').replace('.',',')
    return valor

def dobra(n):
    res= n *2
    return res

def metade(n):
    res = n/2
    return res

def aumentar(n,taxa):
    res = n +(n*taxa/100)
    return res

def diminuir(n,taxa):
    res = n - (n*taxa/100)
    return res
