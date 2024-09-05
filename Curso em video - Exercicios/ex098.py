# Imports
import time

def contagem(inicia, fim, passo):
    '''
    > teste
    
    '''
    print('=='*30)
    print(f'Contagem de {inicia} ate {fim} de {passo} a {passo}')
    time.sleep(2.5)
    if inicia > fim:
        if passo > 0:
            passo = -passo
        elif passo == 0:
            passo-=1
        for n in range(inicia,fim+passo,passo):
            print(n,end=" ",flush=True)
            time.sleep(0.5)
    else:
        for c in range(inicia, fim+passo, passo):
            print(c, end=' ', flush=True)
            time.sleep(0.5)

    print('FIM!')


#PROGRAMA PRINCIPAL
contagem(1,10,1)
contagem(10,0,-2)
print('=='*30)
print('Agora sua vezes de personalizar a contagem.')
i=int(input('Inicio: '))
f=int(input('Fim: '))
p=int(input('Passo: '))
contagem(i,f,p)

help(contagem)