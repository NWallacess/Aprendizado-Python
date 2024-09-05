valores = list()
maior = menor = 0
pmaior = list()
pmenor = list()

for num in range(0,5):
    valores.append(int(input(f'Digeite um valor para ficar na posição {num+1}: ')))
    if num == 0:
        maior=valores[num]
        menor=valores[num]
        pmaior.append(num+1)
        pmenor.append(num+1)
    else:
        if valores [num] == maior:
            pmaior.append(num+1)
        elif valores[num] >= maior:
            maior=valores[num]
            for delete in range(len(pmaior),0,-1):
                pmaior.pop()
            pmaior.append(num+1)
        if valores[num] == menor:
            pmenor.append(num+1)
        elif valores[num] <= menor:
            menor = valores[num]
            for delet in range(len(pmenor),0,-1):
                pmenor.pop()
            pmenor.append(num+1)

print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} na(s) posição(ões) ',end='')
for c in range(0,len(pmaior)):
    print(f'{pmaior[c]}', end='...')
print(f'\nO menor valor digitado foi {menor} na(s) posição(ões) ',end='')
for c in range(0,len(pmenor)):
    print(f'{pmenor[c]}', end='...')
