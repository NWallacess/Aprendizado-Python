num1=int(input('Primeiro valor: '))
num2=int(input('Segundo valor: '))
num3=int(input('Terceiro valor: '))
if num1 > num2 and num1 > num3:
    print('O maior valor digitado é o {}'.format(num1))
elif num2 > num1 and num2 > num3:
    print('O maior valor difitado é o {}'.format(num2))
else:
    print('O maior valor digitado é o {}'.format(num3))
if num1 < num2 and num1 < num3:
    print('O menor valor digitado é o {}'.format(num1))
elif num2 < num3 and num2 < num1:
    print('O menor valor digitado é o {}'.format(num2))
else:
    print('O menor valor digitado é o {}'.format(num3))