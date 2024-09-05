print('='*40)
print('{: ^40}'.format('10 TERMOS DE UMA P.A'))
print("="*40)
num1=int(input('Primeiro termo: '))
num2=int(input('Razão: '))
cont=num1 + (10-1)*num2
for c in range(num1,cont + num2,num2):
    print('{}'.format(c), end='=>')
print('Acabou')