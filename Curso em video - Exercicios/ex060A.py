num = int(input('Digite um numero para calcular seu fatorial: '))
fatorial=1
print('Calculando {}! ... '.format(num),end='')
while not num ==0:
    fatorial=fatorial*num
    if num != 1:
        print('{} X '.format(num), end='')
    else:
        print('{} = {}'.format(num,fatorial), end='')
    num-=1