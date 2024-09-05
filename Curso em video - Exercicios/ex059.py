from time import sleep
num1 = int(input('Primeiro valor: '))
sleep(0.5)
num2 = int(input('Segundo valor: '))
opção = 0
sleep(0.5)
while not opção == 5:
    print('-'*5,'Opções','-'*5)
    print('   [1] SOMA\n   [2] MULTIPLICAÇÃO\n   [3] MAIOR\n   [4] NOVOS VALORES\n   [5] SAIR DO PROGRAMA.')
    opção = int(input('>>> Qual é sua opcão? '))
    sleep(.5)
    if opção == 1:
        print('{} + {} = {}'.format(num1,num2,num1+num2))
        sleep(0.5)
    elif opção == 2:
        print('{} X {} = {}'.format(num1,num2,num1*num2))
        sleep(.5)
    elif opção == 3:
        if num1 >num2:
            print('O valor {} é maior que o valor [ > ] {}'.format(num1,num2))
            sleep(.5)
        else:
            print('O valor {} é maior que o valor [ > ] {}'. format(num2,num1))
            sleep(.5)
    elif opção == 4:
        num1 = int( input ('Primeiro valor: '))
        sleep(0.5)
        num2 = int( input ('Segundo valor: '))
    elif opção >5 and opção <1 or opção == '':
        print('Opção invalida!!! Insira opções validadas')

print('FINALIZANDO...')