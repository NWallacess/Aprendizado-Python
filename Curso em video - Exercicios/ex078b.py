valores = list()
menor = maior = 0

for num in range(0,5): 
    valores.append(int(input(f'Digite um valor para ficar na posição {num+1}: ')))
    if num == 0:
        maior = menor = valores[num]
    else:
        if valores[num] > maior:
            maior = valores[num]
        if menor > valores[num]:
            menor = valores[num]

print('='*30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior: 
        print(f'{i+1}', end='...')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i, v in  enumerate(valores):
    if v == menor:
        print(f'{i+1}', end='...')