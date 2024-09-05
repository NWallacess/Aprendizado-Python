Brasileirão = ('Palmeiuras SP', 'Gremio', 'Atletico Mineiro', 'Flamengo', 'Botafogo', 'Red Bull Bragantino', 'Fluminense', 'CA Paranaense', 'Internacional',
               'Fortaleza', 'São Paulo', 'Cuiabá Esporte Clube', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goias', 'Coritiba', 'América')
c = 'Vasco'
print('Os 5 primeiros colocados foi: ')
for cont in range(0, 5):
    print(f'{Brasileirão[cont]}')
print('---'*10)
print('Os 4 ultimos da tabela: ')
for cont in range(4,0,-1):
    print(f'{Brasileirão[-cont]}')
print('---'*10)
print(f'{sorted(Brasileirão)}')
print('---'*10)
print(f'A posição da Vasco na tabela é {Brasileirão.index(c)+1}')
