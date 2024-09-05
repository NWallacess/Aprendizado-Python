dia=int(input('Quantos dias alugados? '))
km=float(input('Quantos kilometros rodados? '))
pago= (dia*60) + (km * 0.15)
print('O valor pagor é {:.2f} reais.'.format(pago))