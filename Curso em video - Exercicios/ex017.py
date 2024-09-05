'''cateto_oposto=float(input('Informe o cateto oposto: '))
cateto_adj=float(input('informe o cateto adj: '))
hipotenusa=((cateto_oposto**2)+(cateto_adj**2))**(1/2)
print('A hipotenusa do trinagulo retangulo é {:.2f}.'.format(hipotenusa))'''

from math import hypot
co=float(input('Informe o cateto oposto: '))
ca=float(input('Informe o cateto adjacente: '))
hi=hypot(ca,co)
print('A hipotenusa do triangulo é {:.2f}'.format(hi))
