viagem=float(input('Para quão longe você vai viajar(Km)? '))
if viagem<=200:
    print('O valor da passagem vai ser R${}'.format(viagem*0.5))
else:
    print('O valor da passagem vau ser R${}'.format(viagem*0.45))