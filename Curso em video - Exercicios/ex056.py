cont_mulhere=0
idade_homen=0
nome_homem_idade=''
soma_idade=0
for c in range(1,5):
    print('='*10,'{}ª Pessoa'.format(c),'='*10)
    nome=input('Nome: ').strip()
    idade=int(input('Idade: '))
    sexo=input('Sexo [M/F]: ').upper().strip()
    soma_idade+=idade
    if sexo == 'M':
        if idade > idade_homen:
            idadehomen = idade
            nomehomemidade= nome
    else:
        if idade < 20:
            cont_mulhere+=1
media=soma_idade/4
print('''A media de idade do grupo é de {}
O homem mais velho tem {} anos e se chama {}
Ao todo são {} com menos de 20 anos'''.format(media,idade_homen,nome_homem_idade,cont_mulhere))