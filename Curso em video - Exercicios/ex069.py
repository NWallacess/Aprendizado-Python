cont= contm = contf = 0
while True:
    print('='*30)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('='*30)
    idade = int(input('Idade: '))
    sex = ' '
    while sex not in 'MF':
        sex=input('SEXO [F/M]: ').strip().upper()[0]
    if sex =='F' and idade<20:
        contf +=1
    if idade >= 18:
        cont+=1
    if sex == 'M':
        contm +=1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar [S/N] ? ').strip().upper()[0]
    if continuar == 'N':
        break

print('='*30)
print(f'''Total de pessoas com mais de 18 anos: {cont}
Ao todo temos {contm} homens cadastrados.
E temos {contf} mulheres com menos 20 anos.
''')