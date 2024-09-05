print('Calculadora de fatorial. ')
num = int( input( 'Digite um numero para calcular o fatorial dele: '))
fatorial = 1
print('Calculando {0}! ...\n{0}! = '.format(num), end='')
for num in range(num,0,-1):
    if num != 1:
        print('{} x '.format(num),end='')
        fatorial *= num
    else:
        print('{} = {}'.format(num,fatorial))