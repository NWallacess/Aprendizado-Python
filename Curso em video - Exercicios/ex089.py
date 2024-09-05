alunos= []
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    alunos.append([nome, [nota1, nota2], media])
    res = input('Quer continuar [S/N]: ').upper()
    if 'N' in res:
            break
print('=='*20)
print(f'{'Nº':<4}{'Nome':<10}{'Media':>8}')
print('__'*20)
for c in range(0, len(alunos)):
    print(f'{c:<4}{alunos[c][0]:<10}{alunos[c][2]:>8.1f}') 
while True: 
    res = int(input('Deseja mostrar a nota de que alunos? [999 para interromper]:  '))
    if res == 999:
        break
    print(f'Notas de {alunos[res][0]} são {alunos[res][1]}. ')
    print('__'*20)
print('Programa finalizados.')