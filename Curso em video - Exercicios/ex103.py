#Crição de funçções
def ficha(j='<Desconhecido>', g= 0):
    return f'O jogador {j} fez {g} gol(s) no campeonato. '


#Codigo principal
print('--'*10)
jogador = input('Nome do jogador: ').capitalize()
gols = input('Numero de gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols=0
if jogador.strip() == '':
    print(ficha(g=gols))
else:
    print(ficha(jogador, gols))