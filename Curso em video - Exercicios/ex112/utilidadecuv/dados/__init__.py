def validador(txt):
    txt = txt.strip()
    if ',' in txt:
            txt = txt.replace(',','.')
    x = txt.isnumeric()
    if x == True:
        txt = float(txt)
    else:
        while True:
            print(f'O valor "{txt}" é invalido. Digite apanas numeros ou "," ')
            txt = input('Digite um valor: R$')
            txt = txt.strip()
            if ',' in txt:
                txt = txt.replace(',','.')
            x = txt.isnumeric()
            if x == True:
                txt = float(txt)
                break
    return txt
             


    