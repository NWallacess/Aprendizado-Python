valores = list()
while True:
    n = int(input('Digite um numero:'))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    r = input('Deseja continuar [S/N]? ').split()
    if r == 'N' or r == 'n':
        break

valores.sort()
print(f'Os valores adicionados são {valores}')