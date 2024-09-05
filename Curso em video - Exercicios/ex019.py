'''import random
aluno1=input('Informe o nome do primeiro aluno: ')
aluno2=input('Informe o nome do segundo aluno: ')
aluno3=input('Informe o nome do terceiro aluno?: ')
aluno4=input('Informe o nome do quarto aluno: ')
print('O primeiro aluno é {}'.format(random.choice([aluno1,aluno2,aluno3,aluno4])))'''

from random import choice
n1=input('Aluno 1:')
n2=input('Aluno 2:')
n3=input('Aluno 3:')
n4=input('Aluno 4:')
lista=[n1,n2,n3,n4]
print('O aluno escolhido é {}'.format(choice(lista)))