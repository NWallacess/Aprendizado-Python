lista= ('Lápis',1.75,'Borracha',2,'Caderno',15.9,'Estojo',25,'Transferidor',4.2,'Compasso',9.99,'Mochila',120.32,'Canetas',22.3,'Livros',34.9)
print('='*50)
print('{:^50}'.format('LISTAGEM DE PRODUTOS'))
print('='*50)
for pos in range(0, len(lista)):
    if pos % 2==0:
        print(f'{lista[pos]:.<40}',end='')
    else:
        print(f'R$:{lista[pos]:>7.2f}')
print('='*50)
    

