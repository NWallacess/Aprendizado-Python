num1=int(input('Digite um numero:'))
cont=0
for c in range(1,num1+1):
    if num1 % c ==0:
        cont= cont+1
        print('{}'.format(c), end=' ')
    else:
        print('\033[31m{}\033[m'.format(c), end=' ')
if cont ==2:
    print('''
O numero {} foi divisivel apenas duas vezes, 1 e ele mesmo.
Portanto ele é primo!'''.format(num1))
else:
    print('''O numero {} foi divisivel {} vezes
Portanto ele não é um numero primo.'''.format(num1,cont))