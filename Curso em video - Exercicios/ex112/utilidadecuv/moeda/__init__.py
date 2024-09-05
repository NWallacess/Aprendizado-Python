def moeda(txt):
    res = 'R$' + str(f'{txt:.2f}').replace('.',',')
    return res

def dobra(num=0, formato=True):
    res= num *2
    if formato == True:
        res = 'R$' + str(f'{res:.2f}').replace('.',',')
    return res

def metade(num=0,formato=True):
    res = num/2
    if formato == True:
        res = 'R$' + str(f'{res:.2f}').replace('.',',')
    return res

def aumentar(num=0,taxa=0,formato=True):
    res = num +(num*taxa/100)
    if formato ==True:
        res = 'R$' + str(f'{res:.2f}').replace('.',',')
    return res

def diminuir(num=0,taxa=0,formato=True):
    res = num - (num*taxa/100)
    if formato == True:
        res = 'R$' + str(f'{res:.2f}').replace('.',',')
    return res

def resumo(valor= 0, porcentagema= 0, porcentagemr=0):
    print('-' * 30)
    print('ANALISANDO PREÇO'.center(30))
    print('-' * 30)
    print(f'Preço analisado:\t{(moeda(valor))}')
    print(f'Metado do preço: \t{(metade(valor))}')
    print(f'Dobro do preço: \t{(dobra(valor))}')
    if porcentagema > 9:
        print(f'{porcentagema}% de aumento: \t{(aumentar(valor,porcentagema))}')
    else:
        print(f'{porcentagema}% de aumento: \t\t{(aumentar(valor, porcentagema))}')
    if porcentagemr > 9:
        print (f'{porcentagemr}% de redução: \t{(diminuir(valor,porcentagemr))}')
    else:
        print(f'{porcentagemr}% de redução: \t\t{(diminuir(valor, porcentagemr))}')
    return '-' * 30