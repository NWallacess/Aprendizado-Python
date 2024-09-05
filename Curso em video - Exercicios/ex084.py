informacaosPessoais = []
bancoDeDados = []
maiorPeso = menorPeso = 0

while True:
    informacaosPessoais.append(input('Nome: '))
    informacaosPessoais.append(float(input('Peso: ')))
    if len(bancoDeDados) == 0:
        maiorPeso = menorPeso = informacaosPessoais[1]
    else:
        if informacaosPessoais[1] > maiorPeso:
            maiorPeso = informacaosPessoais[1]
        if informacaosPessoais[1] < menorPeso:
            menorPeso = informacaosPessoais[1]
    bancoDeDados.append(informacaosPessoais[:])
    informacaosPessoais.clear()
    continuar = input('Quer continuar [S/N]: ').upper()
    if continuar in 'N':
        break

print(f'Ao todo, foi cadastrados {len(bancoDeDados)} pessoas.')

print(f'O maior peso listado foi de {maiorPeso:.2f}Kg. Peso de ', end='')
for p in bancoDeDados:
    if p[1] == maiorPeso:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso listado for de {menorPeso:.2f}kg. Peso de ', end='')
for p in bancoDeDados:
    if p[1] == menorPeso:
        print(f'{p[0]}', end=' ')
