valor = [[],[]]

for n in range(0,7):
    num = int(input(f'Digite o {n+1}º valor:  '))
    if num % 2 == 0:
        valor[0].append(num)
    if num % 2 == 1:
        valor[1].append(num)
valor[0].sort()
valor[1].sort()
print('=='*40)
print(f'Os valores pares digitados foram: {valor[0]}')
print(f'Os valores impares digitados foram: {valor[1]}')