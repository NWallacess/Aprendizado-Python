import moeda

num = int(input('Digite um preço: R$'))
print(f"A metade de R${num} é R${moeda.metade(num)}\nO dobro de R${num} é R${moeda.dobra(num)}.\nAumentado 10%, temos R${moeda.aumentar(num,10)}.\nDiminuindo 10%, temos R${moeda.diminuir(num,10)}.")