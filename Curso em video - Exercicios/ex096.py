def area(larg, compr):
    a = (l * c)
    print(f'A area do terreno {l:.2f}m X {c:.2f}m e de {a:.2f} m²')

#programa principal
print()
print('Controle de Terreno')
print('--'*10)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l,c)