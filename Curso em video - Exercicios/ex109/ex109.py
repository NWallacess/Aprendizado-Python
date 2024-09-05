import moeda

valor = float(input('Digite um valor: R$ '))
print(f'Metade do valor do {moeda.moeda(valor)} é {(moeda.metade(valor))}')
print(f'O dobro do valor de {moeda.moeda(valor)} é {(moeda.dobro(valor))}')
print(f'Aumentando o valor em 10% da {moeda.aumentar(valor,10)}')
print(f'Dimuindo o valor em 13% da {moeda.diminuir(valor,13)}')