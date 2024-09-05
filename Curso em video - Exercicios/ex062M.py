print('='*40)
print('{: ^40}'.format('GERADOR DE P.A.'))
print('='*40)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
cont = 11
cont_termos = 0
while not cont ==0:
    if cont >1:
        print('{}'.format(primeiro), end='=>')
        primeiro += razão
        cont-=1
        cont_termos += 1
    elif cont ==1:
        print('Pause')
        cont = int( input('Quantos termos você que monstrar a mais? '))
        if cont == 0:
            cont = 0 
        else:
            cont+=1
print('Progresão finalizada com {} termos mostrados'.format(cont_termos))