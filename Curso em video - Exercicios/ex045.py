from random import shuffle
from time import sleep
print('{:=^20}'.format('JOKENPÔ'))
print('''Suas opções.
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
opcao= int(input('Qual é sua opção? '))
comp=[0,1,2]
shuffle(comp)
comp_opcao=comp[0]
lista=('PEDRA','PAPEL','TESOURA')
print('JAN')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
print('=-'*30)
print('O computador jogou {}'.format(lista[comp_opcao]))
print('O jogador jogou {}'.format(lista[opcao]))
print('-='*30)
if comp_opcao==0:
    if opcao ==0:
        print('EMPATE')
    elif opcao==1:
        print('JOGADOR VENCEU')
    elif opcao==2:
        print('JOGADOR PERDEU')
    else:
        print('OPÇÃO INVALIDA')
elif comp_opcao==1:
    if opcao ==1:
        print('EMPATE')
    elif opcao==2:
        print('JOGADOR VENCEU')
    elif opcao==0:
        print('JOGADOR PERDEU')
    else:
        print('OPÇÃO INVALIDA')
elif comp_opcao==2:
    if opcao ==2:
        print('EMPATE')
    elif opcao==0:
        print('JOGADOR VENCEU')
    elif opcao==1:
        print('JOGADOR PERDEU')
    else:
        print('OPÇÃO INVALIDA')