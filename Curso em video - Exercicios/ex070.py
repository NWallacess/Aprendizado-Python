print('='*50)
print('{:^50}'.format('LOJA SUPER BARATÃO'))
print('='*50)
menorpreco = cont = soma = 0
nome_menorpreco = ' '

while True:
    nom = input('Nome do Produto: ').capitalize()
    preco= float(input('Preço: '))
    if menorpreco == 0: 
        menorpreco = preco
        nome_menorpreco = nom
    elif menorpreco>preco:
        menorpreco = preco
        nome_menorpreco=nom
    soma+= preco
    if preco > 1000:
        cont +=1
    op = ' '
    while op not in 'NS':
        op=input('Deseja continuar [N/S]: ').strip().upper()[0]
    if op == 'N':
        break

print('-'*50)
print(f'''O total da compra for R${soma:.2f}
Temos {cont} produtos custando a mais de R$1000
O produto mais barato foi {nome_menorpreco} que custa R${menorpreco}
''')
