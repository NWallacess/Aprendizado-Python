soma = 0
cont = 0
for num in range(1, 7):
    num = int(input("Informe um numero: "))
    if num % 2 == 0:
        cont = cont = 1
        soma = soma+num
print('Você informou {} valores pares e a soma é {}'.format(cont, soma))
