from datetime import datetime
pessoa={}
pessoa['Nome'] = input('Nome: ')
nasc = int(input('Ano de nascimentos: '))
pessoa['Idade'] = datetime.now().year - nasc
pessoa['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['CTPS'] != 0:
    pessoa['Ano que assinou a carteira pela 1º'] = int(input('Ano que assinou a carteira pela 1º: '))
    pessoa['Salario']= float(input('Salario Atual: '))
    pessoa['Ano da aposentadoria'] = pessoa['Ano que assinou a carteira pela 1º']+35
print('=='*30)
for k,v in pessoa.items():
    print(f'  - {k} é igual {v}')