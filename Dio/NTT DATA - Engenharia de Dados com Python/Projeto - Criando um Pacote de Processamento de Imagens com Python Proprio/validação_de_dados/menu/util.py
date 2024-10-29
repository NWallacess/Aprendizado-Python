def linhas():
    print('~~'*20)


def titulo(txt): 
    linhas()
    print(txt.center(40))
    linhas()


def menu(lista):
    titulo('MENU PRINCIPAL')
    cont=0
    for item in lista:
        print(f'\033[1;33m{cont+1}\033[m','-',f'{lista[cont]}')
        cont+=1
    linhas()
    escolha = leiaint('Opção: ')
    titulo(f'opção {escolha}')
    return escolha
