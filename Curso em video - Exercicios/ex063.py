print('~~'*20)
print('{: ^40}'.format('Sequência de Fibonacci'))
print('~~'*20)
termo = int(input('Quantos termos você deseja ver da sequência? '))
n1=0
n2=0
n3=0
cont= 0
while not cont == termo:
    n3 = n2 + n1
    if n1 == 0:
        n1 = 1
    else:
        n1 = n2
        n2 = n3
    cont+= 1
    print('{}'.format(n3),end=' => ')
print('FIM')