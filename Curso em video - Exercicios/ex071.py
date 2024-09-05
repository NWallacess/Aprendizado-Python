print('='*50)
print('{:^50}'.format('BANCO CEV'))
print('='*50)
total50 =total20 = total10 = total1 = 0
valor = int(input('Que valor você deseja sacar? R$'))

while True:
    if valor>= 50:
        total50 +=1
        valor-= 50
    elif 20 <=valor:
        total20+=1
        valor-=20
    elif 10<=valor:
        total10 += 1
        valor-=10
    elif 1<=valor:
        total1+=1
        valor-=0
    elif 0==valor:
        break

if total50 != 0:
    print(f'Total de {total50} cédulas de 50 reais')
if total20 != 0:
    print(f'Total de {total20} cédulas de 20 reais')
if total10 != 0:
    print(f'Total de {total10} cédulas de 10 reais')
if total1 != 0:
    print(f'Total de {total1} cédulas de 1 real')