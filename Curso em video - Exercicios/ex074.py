from random import randint
maior = menor = 0
num = (randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))
print(f'Os valores sorteados foram: {num[0]} {num[1]} {num[2]} {num[3]} {num[4]}.')

for c in range(0,len(num)):
    if c == 0:
        maior = num[c]
        menor = num[c]
    elif c != 0:
        if maior <= num[c]:
            maior = num[c]
        if menor >= num[c]:
            menor = num[c]

print(f'O maior valor sorteado foi: {maior}.\nO menor valor sorteado foi: {menor}.')
