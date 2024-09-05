print('='*40)
print('{: ^40}'.format('10 TERMOS DE UMA P.A.'))
print('='*40)   
n1= int(input('Primeiro termo: '))
n2= int(input('Razão: '))
c = 10
while not c == 0:
    print('{}'.format(n1), end='=>')
    c -= 1
    n1+= n2
print('Acabou')