n=int(input('Digite um numero:'))
print('\033[7;40mAnalisando o numero {}, tem como sucessor {} e antecessor {}.\033[m'.format(n, (n+1), (n-1)))