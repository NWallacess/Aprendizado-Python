nota1= float(input('Nota da PRIMEIRA avaliação: '))
av2= float(input('Nota da SEGUNDA avaliação: '))
media = ( nota1 + av2 ) / 2
print('Sua média é {:.2f}'.format(media))
if media >=7:
    print('O aluno esta \033[1;32mAPROVADO!!\033[m')
elif media>=5:
    print('O aluno esta de recuperação.')
else:
    print('O aluno esta \033[1;31mREPROVADO.\033[m')