#funções
def leiaint(txt):
    while True:
        try:
            num = int(input(txt)).strip()
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


#Codigo principal
print('--'*20)
z = leiafloat('Digite um nuemro inteiro: ')
r = leiaint('Digite um numero real: ')
print(f'O valor inteiro digitado foi {z} e o real {r} ')