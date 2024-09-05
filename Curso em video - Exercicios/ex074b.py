from random import randint
maior = menor = 0
num = (randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))
print('Os valores sorteados foram: ', end=' ')
for n in num:
    print(f'{n}',end=' ')
print(f'\nO maior valor sorteado foi: {max(num)}.\nO menor valor sorteado foi: {min(num)}.')