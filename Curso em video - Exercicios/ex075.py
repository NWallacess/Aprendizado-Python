num1=int(input('Digite um numero: '))
num2=int(input('Digite outro numero: '))
num3=int(input('Digeite mais um numero: '))
num4=int(input('Digite o ultimo numero: '))
numall= (num1,num2,num3,num4)
posição = cont_par= cont_tres = 0
print(f'Você digitou os valores: {numall}')
print(f'O valor 9 apareceu {numall.count(9)} vezes')
print('A primeira aparição do valor 3 foi na posição: ',end='')
for z in range(0,4):
    if numall[z] == 3:
        posição = z + 1
        print(posição)
        cont_tres+=1
if cont_tres ==0:
    print('N/A')
print('Os valores pares digitados: ', end='')
for n in range(0,4):
    if numall[n] % 2 ==0:
        print(numall[n],end=' ')
        cont_par+=1
if cont_par == 0:
    print('N/A')
