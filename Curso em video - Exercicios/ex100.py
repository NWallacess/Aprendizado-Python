#import de biblioteca
import random
import time

#rotinas
def sort(list, valores):
    cont = 0
    while cont < valores:
        cont+=1
        list.append(random.randint(0,9))
    print(f'Sorteando {valores} da lista: ', end='')
    for numero in list:
        print(numero, end=' ',flush=True)
        time.sleep(1)
    print('PRONTO! ')
def somaPar(list):
    soma = 0
    for numeroPar in list:
        if numeroPar % 2 == 0:
            soma+=numeroPar
    print(f'Somando os valores pares da lista {list}.')
    time.sleep(2)
    print(f'  >Resultado da soma é igual a {soma}.')
            

# Codigo principal
num = []
sort(num,6)
time.sleep(1)
somaPar(num)