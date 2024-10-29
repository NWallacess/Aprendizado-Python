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
            print(f'\033[1;31mERRO!\033[m \033[31m Digite um numero decimal.\033[m')
            num = input(f'{txt}').strip()
    return num

def leiaSTR(txt):
    strin = input(f'{txt}').strip()
    while True:
        try:
            strin = str(strin)
            break
        except:
            print(f'\033[1;31mERRO!\033[m \033[31m Digite novamente.\033[m')
            strin = input(f'{txt}').strip()
    return strin