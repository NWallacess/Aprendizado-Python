print('Programa para calcular a existência de triangulo.')
l1=float(input('Digite lado 1: '))
l2=float(input('Digite lado 2: '))
l3=float(input('Digite lado 3: '))
if l1+l2>l3 and l2+l3>l1 and l3+l1>l2:
    if l1==l2==l3:
        print('Com os seguementos {}, {} e {} é \033[1;32mPOSSÍVEL\033[m criar um triangulo e ele seria \033[1mEQUILÁTERO\033[1'.format(l1,l2,l3))
    elif l1==l2 or l1==l3 or l3==l1:
        print('Com os seguementos{}, {} e {} é \033[1;32mPOSSÍVEL\033[m criar um triangulo e ele seria \033[1mISÓSCELES\033[m'.format(l1,l2,l3))
    else:
        print('Com os seguementos {}, {} e {} é \033[1;32mPOSSÍVEL\033[m cria um triangulo e ele seria \033[1mESCALENO\033[m'.format(l1,l2,l3))
else:
    print('Com os seguementos {}, {} e {} é \033[1;31mIMPOSSÍVEL\033[m cria um triangulo'.format(l1,l2,l3))
