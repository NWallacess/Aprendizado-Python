sexo = input('Digite seu sexo [M/F]:').strip().upper()[0]
while sexo not in 'MmFf':
    sexo=input('Dado Invalidado. Digite seu sexo: ').upper().strip() 
print("Seu sexo é {}".format(sexo))