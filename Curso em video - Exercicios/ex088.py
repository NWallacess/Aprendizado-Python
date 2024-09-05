import random 
import time

print('=='*20)
print(f'{'JOGA NA MEGA SENA':^40}')
print('=='*20)
sorteio = int(input('Quantos jogos você quer que eu sorteie? '))
print('=='*20)
print(f'{f'SORTEANDO {sorteio} JOGOS':^40}')
print('=='*20)
temp = 0
num = []
num_temp = []
for s in range(0,sorteio):
    for c in range(0,6):
        temp= random.randint(1,60)
        if temp in num_temp:
            while True:
                temp = random.randint(1,60)
                if num_temp.count(temp) == 0:
                    break
        num_temp.append(temp)
    num_temp.sort()
    num.append(num_temp[:])
    num_temp.clear()
for n , l in enumerate(num):
    print(f'Jogo {n+1}: {l}')
    time.sleep(1)
print('=='*20)