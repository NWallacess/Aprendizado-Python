def factoria(n):
    f=1
    for c in range(1,n+1):
        f*=c
    return f


num = int(input('Digite um numero: '))
fac = factoria(num)
print(f'O fatorial do {num} é {fac}')