dicpessoas = {}
listpessoas= []
media = somaIdade = mulheres = 0
while True:
    dicpessoas['Nome'] = input('Nome: ')
    dicpessoas['Sexo'] = input('Sexo [M/F]: ').capitalize()[0]
    if dicpessoas['Sexo'] != 'M' and dicpessoas['Sexo'] != 'F':
        while True:
            print('ERRO! Digite M ou F.')
            dicpessoas['Sexo'] = input('Sexo [M/F]: ').capitalize()[0]
            if dicpessoas['Sexo'] == 'M' and dicpessoas['Sexo'] == 'F':
                break
    if dicpessoas['Sexo']=='F':
        mulheres+=1
    dicpessoas['Idade'] = int(input('Idade: '))
    somaIdade += dicpessoas['Idade']
    res = input('Deseja continuar [S/N]? ').capitalize()[0]
    if res != 'N' and res != 'S':
        while True:
            print('ERRO! Digite "S" para sim ou "N" para não. ')
            res = input('Deseja continuar[S/N] ? ').capitalize()[0]
            if res == 'S' or res == 'N': 
                break
    listpessoas.append(dicpessoas.copy())
    if res == 'N':
        break

media = somaIdade/len(listpessoas)
print('=='*30)
print(f'A) Ao todo foi cadastrado {len(listpessoas)} na base.')
print(f'B) A media de idade das pessoas cadastradas é {media}')
if mulheres!=0:
    print('C) A(s) mulher(es) cadastrada(s) foi/foram: ',end='')
    for p in listpessoas:
        if p['Sexo'] == 'F':
            print(f'{listpessoas[p]['Nome']}',end='; ')
    print()
else:
    print('C) Não foi cadastrado nenhuma mulher')
print('D) Lista de pessoas que estão acima da idade média: ')
for p in range(0,len(listpessoas)):
    if listpessoas[p]['Idade'] >= media:
        print(listpessoas[p])