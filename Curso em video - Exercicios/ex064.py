c = cont= 0
n= int(input('Digite um numero: [999 para parar] '))
while n != 999:
    c+= n
    n= int(input('Digite um numero: [999 para parar] '))
    cont+=1
print('Voce digitou {} numero e a soma entre eles é {}'.format(cont,c))