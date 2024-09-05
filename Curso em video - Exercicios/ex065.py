num = soma = menor= maior= cont= 0
opção = ''
while not opção == 'N':
    num = int(input('Digite um valor: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    if cont > 1:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
    opção = input('Quer continuar? [S/N] ').strip().upper()[0]
print('você digito {} numeros e a média foi {}\nO maior valor foi {} e o menor valor for {}.'.format(cont,soma/cont,maior,menor))
