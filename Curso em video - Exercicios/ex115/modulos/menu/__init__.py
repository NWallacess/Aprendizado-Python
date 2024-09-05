def leiaint(txt):
    while True:
        try:
            num = int(input(txt))
        except(ValueError,TypeError):
            print(f'\033[1;31mERRO!\033[m \033[31m Digite um numero inteiro.\033[m')
            continue
        else:
            return num


def leiafloat(txt):
    num = input(f'{txt}').strip()
    while True:
        try:
            num = float(num)
            break
        except:
            print(f'\033[1;31mERRO!\033[m \033[31m Digite um numero inteiro.\033[m')
            num = input(f'{txt}').strip()
    return num

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




