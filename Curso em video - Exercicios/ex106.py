def newhelp(txt):
    help(f'\033[3m{txt}')


#Codigo Principal 
while True:
    print('=='*20)
    função = input('Escolhar um função ser explicada: ')
    newhelp(função)
    escolha = input('Quer continuar[S/N]: ').upper()[0]
    if escolha == 'N':
        break