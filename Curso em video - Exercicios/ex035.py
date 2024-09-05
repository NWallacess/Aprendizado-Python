print('-=' * 30)
print('Analisador de triangulo')
print('-=' * 30)
s1=float(input('Primeiro seguemento: '))
s2=float(input('Segundo seguemento: '))
s3=float(input('Teceiro seguemento: '))
if s1+s2>s3 and s2+s3>s1 and s3+s1>s2:
    print('Com os seguementos {}, {} e {} é \033[1;32mPOSSIVEL\033[m fazer um triangulo.'.format(s1,s2,s3))
else:
    print('Com os seguementos {}, {} e {} é \033[1;31mIMPOSSIVEL\033[m fazer um triangulo.'.format(s1,s2,s3))