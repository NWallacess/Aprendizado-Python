palavras = ['APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO']

for p in palavras:
    print(f'\nNa palavra {p} temos',end=' ')
    for letra in p:
        if letra.lower() in 'aeiuo':
            print(f'{letra.lower()}', end=' ')


