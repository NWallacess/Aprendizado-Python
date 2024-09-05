while True :
    n=int(input('Deseja ver a tabudada de qual numero? '))
    print('-'*12)
    if n<0:
        break
    for c in range (1,11):
        print(f'{n} x {c} = {n*c}')
    print('-'*12)
print("PROGRAMA DE TABUADO ENCERRADO, volte sempre!!!")