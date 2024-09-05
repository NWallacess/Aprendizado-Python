expresao=input('Digite um expresão numerica:' ).strip()
lista = []
for simb in expresao:
    if simb == '(':
        lista.append('(')
    elif simb== ')':
        if len(lista)>0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Essa expresão e valida!!!')
else:
    print('Essa expresão não e possivel ')