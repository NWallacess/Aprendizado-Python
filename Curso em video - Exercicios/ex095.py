#criando as principais variaveis do cod
jogador = dict()
time =  list()
aproveitamento = list()

#criando cod para cadastro dos jogadores.
while True:
    jogador.clear()
    jogador['Nome'] = input('Nome do jogador: ').capitalize()
    jogos = int(input(f'Quantos partidas o {jogador["Nome"]} jogou? '))
    for a in range(0,jogos):
        aproveitamento.append(int(input(f'Quantos gols na partida {a+1}ª? ')))
    jogador['Gols'] = aproveitamento[:]
    jogador['Total'] = sum(aproveitamento)
    aproveitamento.clear()
    time.append(jogador.copy())
    while True:
        continuar = str(input('Quer continuar [S/N]? ')).upper()[0]
        if continuar != 'N' and continuar != 'S':
            print('ERRO! Escolha entre "S" para sim ou "N" para não.')
        else:
            break
    if continuar == 'N':
        break

#Analisando as informções lidas
print('=='*30)
print(f'{'Cod':<4}', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('=='*30)
for k,v in enumerate(time):
    print(f'{k:<4}',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()

while True:
    indice = int(input('Mostra dados de qual jogador (999 para parar)? '))
    if indice == '999':
        break
    if indice >= len(time):
        print('ERRO! Digite um dado valido! ')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[indice]["Nome"]}')
        for i,j in enumerate(time[indice]['Gols']):
            print(f'    No jogo {i+1} fez {j} gols.')

#Encerramento do programa
print('<<<Volte Sempre>>>')