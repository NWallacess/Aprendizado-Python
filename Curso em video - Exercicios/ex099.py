#imports
import random
import time


#Rotinas
def maior(*num):
    print('=='*20)
    time.sleep(1)
    print('Analisando os valores passados...')
    time.sleep(1)
    maior_num = 0
    for c in num:
        print(c, end=' ',flush=True)
        time.sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo. ')
    time.sleep(1)
    for n in range(0, len(num)):
        if n == 0:
            maior_num = num[n]
        if maior_num <= num[n]:
            maior_num = num[n]
    print(f'O maior valor informado foi {maior_num}. ')
    time.sleep(1)

#Codigo principal
maior(random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9))
maior(random.randint(0,9),random.randint(0,9),random.randint(0,9))
maior(random.randint(0,9),random.randint(0,9))
maior(random.randint(0,9))
maior()