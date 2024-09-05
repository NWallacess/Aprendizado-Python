salario=float(input('Quanto é o salario do funcionario? '))
if salario <= 1200:
    print('O salario passa a ser R${:.2f}'.format(salario * 1.15))
else:
    print('O salario passa a ser R${:.2f}'.format(salario * 1.10))