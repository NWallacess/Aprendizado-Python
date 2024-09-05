lista=[]
pares=[]
impares=[]
while True:
    lista.append(int(input('Digite um valor: ')))
    res = input('Quer continuar (S/N)? ').strip().upper()
    if res == 'N':
        break
for c,v in enumerate(lista):
    if v % 2 == 0:
        pares.append(lista[c])
    if v % 2 == 1:
        impares.append(lista[c])
print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')