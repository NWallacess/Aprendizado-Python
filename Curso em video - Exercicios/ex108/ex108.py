import moeda

num = int(input('Digite um preço: R$'))
print(f"A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}\nO dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobra(num))}.\nAu/mentado 10%, temos {moeda.moeda(moeda.aumentar(num,10))}.\nDiminuindo 10%, temos {moeda.moeda(moeda.diminuir(num,10))}.")