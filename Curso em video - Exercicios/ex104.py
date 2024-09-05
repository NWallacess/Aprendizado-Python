#funções
def leiaint(txt):
    num = input(f'{txt}')
    while True:
        if num.isnumeric():
            num = int(num)
            break
        else:
            print(f'\033[1;31mERRO!\033[m \033[31m Digite um numero inteiro.\033[m')
            num= input(f'{txt}')
    return num


#Codigo principal
print('--'*20)
n = leiaint('Digite um numero: ')
print(f'Você acbou de digitar o numero {n}')