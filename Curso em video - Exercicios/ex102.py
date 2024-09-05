#ROTINAS
def fatorial(numero, show = False):
    '''
    -> calcula o Fatorial de um número.
:param numero> O numero a ser calculado.
:para show: (opcional) Mostra ou não a conta
:return: O valor do fatorial do número.
    '''
    fact=1
    for n in range(numero,0,-1):
        if show == True:
            if n != 1:
                print(f'{n}', end=' x ')
            else:
                print(n, end=' = ')
        fact*=n
    return fact


#Codigo principal
print('--'*20)
print(fatorial(7, show=True))
