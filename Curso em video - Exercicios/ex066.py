s = cont = 0
while True:
    n = int(input('Digite um numero [999 para parar]: '))
    if n == 999:
        break
    s+= n
    cont+=1
print(f'A soma dos {cont} valores é {s}.')