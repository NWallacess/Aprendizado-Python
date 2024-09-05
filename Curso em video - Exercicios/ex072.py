num = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','cartorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
while True:
    opcao = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= opcao <=20:
        break
    print('Opção invalida#####.',end='')

print(f'Vocé digitou o numero {num[opcao]}.')