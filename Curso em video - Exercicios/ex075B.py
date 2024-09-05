num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite o ultimo numero: ')))
print(f'O valores digitados são {num}.')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:    
    print(f'O valor 3 apareceu {num.index(3)}ª posição')
else:
    print('O valor 3 não foi digitado.')
print('O valores pares digitados foram : ', end='')
for n in num:
    if n % 2 ==0:
        print(n, end=' ')
