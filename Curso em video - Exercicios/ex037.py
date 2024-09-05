from time import sleep
num=int(input('Digite um numero: '))
cod=int(input('Digite um [ 1 ] para converte ele em binario\n Digite [ 2 ] para converte ele em octal.\n Digite [ 3 ] para converte ele para hexadecimal:\n Qual é sua opcão: '))
print('CONVERTENDO...')
sleep(2)
if cod==1:
    print('O número {} em binario é igual a {}'.format(num,bin(num)[2:]))
elif cod==2:
    print('O numero {} em octal é igual a {}'.format(num,oct(num)[2:]))
elif cod==3:
    print('O numero {} em hexadecimal é igual a {}'.format(num,hex(num)[2:]))
else:
    print('\033[1;31mDigite uma das opções para converter.\033[m')