jogador = {'Nome': 0, 'Gols': 0, 'Total': 0}
res_das_partidas = []

jogador['Nome'] = input('Nome do jogador: ').capitalize()
partida = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for g in range(0, partida):
    res_das_partidas.append(int(input(f'Quantos gols na {g+1}ª partida: ')))
jogador['Total'] = sum(res_das_partidas)
jogador['Gols']=res_das_partidas[:]

print('=='*30)
print('''
''',
    jogador,
    '''
''')

print('=='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('=='*30)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas. ')
for p,c in enumerate(jogador['Gols']):
    print(f'  => Na partida {p}, fez {c} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')