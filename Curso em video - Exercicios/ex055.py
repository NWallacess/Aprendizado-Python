maispesado=0
menospesado=0
for c in range(1,6):
    peso = float(input('Peso da {}ª: '.format(c)))
    if c == 1:
        maispesado= peso
        menospesado= peso
    else:
        if peso > maispesado:
            maispesado = peso
        if peso < menospesado:
            menospesado = peso

print('''O maior peso lido é de {}Kg
O menor peso lido é de {}Kg'''.format(maispesado,menospesado))