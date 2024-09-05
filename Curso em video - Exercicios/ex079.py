valores=list()

while True:
    n = int(input('Digite um valor: '))
    if valores.count(n) == 0:
        valores.append(n)
        print('Valor adicionando com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = input('Deseja continuar [S/N]? ').strip().upper()
    if continuar == 'N':
        break

valores.sort()
print(f'Os valores digitados são {valores}')