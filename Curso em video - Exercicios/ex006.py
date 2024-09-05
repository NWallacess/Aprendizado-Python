n=int(input('Digite um numero:'))
print('O dobro de \033[34m{0}\033[m é \033[36m{1}\033[m. \nO triplo de \033[34m{0}\033[m é \033[31m{2}\033[m. \nA raiz quadrada de {0} é {3:.2f}.'.format(n, (n*2), (n*3), (n**(1/2))))
