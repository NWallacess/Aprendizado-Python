print('='*40)
print('{: ^40}'.format('GERADOR DE P.A.'))
print('='*40)
p1=int(input('Primeiro termo: '))
r=int(input('Razão: '))
cont=9
mais = 1
cont_termo=0
while mais != 0:
    cont+=mais
    while not cont ==0:
        print('{}'.format(p1), end='=>')
        p1+=r
        cont-=1
        cont_termo+=1
    print('Pausa')
    mais = int(input('Quantos termos você quer a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(cont_termo))