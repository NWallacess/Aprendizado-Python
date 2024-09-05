num = ('Um', 'Dois', 'Tres','Quarta','Cinco','Seis','Sete','Oito', 'Nove', 'Dez', 'Onze', 'Doze','Treze','Quartoze','Quinze','Dezesseis', 'Dezesete','Dezoito','Dezenove','Vinte')

while True:
    escolha = int(input('Escolha um numero de 1 a 20: '))
    if escolha <= 20:
        break
    else: 
        print('Tente novamente. Escolha um numero de 1 a 20: ')
print(f'O numero {escolha} por extenso é {num[escolha-1]}')