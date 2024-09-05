from datetime import date
maioridada=0
menoridade=0
anoatual=date.today().year
for c in range(1,8):
    ano=int(input('Que ano a {}ª pessoa nasceu? '. format(c)))
    idade= anoatual - ano 
    if idade >= 18:
        maioridada = maioridada + 1
    else:
        menoridade = menoridade + 1
print('''Ao todo tivemos {} pessoas maiores de idade
e tambem tivemos {} pessoas menores de idade.
'''.format(maioridada,menoridade))