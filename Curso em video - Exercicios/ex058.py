import random
comp = random.randint(0,10)
cont = 0
acertou = False
print('Sou seu computador. \nEstou pensando em um numero entre 0 à 10...\nVocê consegue adivinhar qual é?')
'''usuario = int(input('Qual é o seu palpite? '))
while usuario != comp:
    print('Errou!!! tente novamente.')
    cont+=1
    usuario=int(input('Dê outro palpite: '))'''
while not acertou:
    usuario = int(input('Qual é seu palpite? '))
    if usuario == comp:
        cont+=1
        acertou = True
    else:
        if usuario>comp:
            cont+= 1
            print('Tente novamente, mas com um valor menor.')
        elif usuario<comp:
            cont+=1
            print('Tente novamente, mas com um valor maior.')
print('Acertou!!! o numero era {}.\nVocê precisou de {} tentativas para conseguir.'.format(comp,cont))