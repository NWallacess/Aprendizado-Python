import random
res=int(input('O computado pensou em um numero de 0 a 5.\nQual numero você acha que ele pensou? '))
num=[0,1,2,3,4,5]
random.shuffle(num)
if num==res:
    print('Parabens!!! Você acertou!!!')
else:
    print('Você errou, mais sorte na proxima vezes.')