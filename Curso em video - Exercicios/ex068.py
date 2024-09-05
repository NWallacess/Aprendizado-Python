from random import randint
cont = 0
while True:
    print('-='*15)
    print('VAMOS JOGAR UM JOGO')
    print('-='*15)
    pc = randint(0,5)
    usuario = int(input('Digite um numero: '))
    decisão = ' '
    while decisão not in 'PI':
        decisão = input("Impar ou par [I/P]: ").strip().upper()[0]
    resultado = (pc + usuario) % 2
    s= usuario + pc
    print(pc)
    print(resultado)
    if decisão == 'I':
        if resultado == 0:
            break
        else:
            cont+=1
            print(f'PARABENS!!! Você ganhou!\nVocê digitou {usuario} e o computador {pc} a soma da {s} que é par.\nVamos de novo!')
    elif decisão == 'P':
        if resultado== 1:
            break
        else:
            cont+=1
            print(f'PARABENS!!! Você ganhou"\nVocê digitou {usuario} eo computador {pc} a soma da {s} que é impar.\nVamos de novo!')

print(f'GAME OVER!!! Você ganhor {cont} vezes')