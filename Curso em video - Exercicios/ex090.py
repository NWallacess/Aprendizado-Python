aluno = {}
aluno['Nome']= input('Nome: ').capitalize()
aluno['Media'] = float(input(f'Media do {aluno["Nome"]}: '))
print('__'*20)
if aluno['Media'] >= 7:
    aluno['Situaçao']= 'Aprovado'
elif 5 <= aluno['Media'] <7:
    aluno['Situaçao']= 'recuperação' 
else:
    aluno['Situaçao'] = 'reprovado'

for k,v in aluno.items():
    print(f'{'-':>2} {k} do aluno é igual a {v}')