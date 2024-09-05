from time import sleep
num1=float(input('Digite um numero: '))
num2=float(input('Digite outro: '))
print('Fazendo comparação entre os valor {} e {}...'.format(num1,num2))
sleep(1)
if num1>num2:
    print('{} e maior que o {}'.format(num1,num2))
elif num2>num1:
    print('{} é maior que o {}'.format(num2,num1))
else:
    print('Os valores são iguais.')