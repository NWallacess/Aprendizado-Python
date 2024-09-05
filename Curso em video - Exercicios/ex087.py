matriz = [[0,0,0], [0,0,0], [0,0,0]]
pares = somaColunas = maiorvalor = 0 

print("Criação de matriz 3x3")
print('=='*20)
for linhas in range(0,3):
    for colunas in range(0,3):
        matriz[linhas][colunas] = int(input(f'Digite um valor para a posição [{linhas}, {colunas}]: '))
        if matriz[linhas][colunas] %2 ==0:
            pares += matriz[linhas][colunas]
        if colunas == 2:
            somaColunas += matriz[linhas][colunas]
        if linhas == 1:
            if maiorvalor == 0:
                maiorvalor = matriz[linhas][colunas]
            if maiorvalor < matriz[linhas][colunas]:
                maiorvalor = matriz[linhas][colunas]

print('=='*15)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end="")
    print()
print('=='*15)
print(f'A soma dos valores pare é {pares}.')
print(f'A soma dos valores da terceira coluna é {somaColunas}')
print(f'O maior valor da segunda linha é {maiorvalor}')