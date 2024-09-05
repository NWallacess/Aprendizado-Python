from random import randint
from time import sleep
from operator import itemgetter

print(f'{'=='*5}Sorteado os valores{'=='*5}')
jogadores = {}
ranking = list()
for j in range(1,5):
    jogadores [f'{j}º jogador'] = randint(1,6)
for j, n in jogadores.items():
    print(f'  - {j} tirou {n} no dado. ')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse='True')
print('='*39)
print(f'''{'==':>6} RANKING DOS JOGADORES {'==':<5}''')
for i, v in enumerate(ranking):
    print(f'{'-':>5} {i+1}º Lugar: {v[0]} com {v[1]}')
    sleep(1)
