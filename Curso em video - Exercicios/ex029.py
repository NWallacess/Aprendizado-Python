velo=float(input('Qual é a velocidade que ele passou?'))
multa=(velo-80)*7
if velo<=80:
    print('Passou dentro dos limites de velocidade.')
else:
    print('Passou a {}Km que acima do limite de velocidade que é 80Km/h.\nA multa é R${:.2f}.'.format(velo,multa))
