from datetime import date
ano=int(input('Qual é o ano de hoje? Digite 0 caso queira ver o ano atual. '))
if ano == 0:
    ano = date.today().year
if ano%4==0 and ano%100 !=0 or ano% 400==0:
    print('O ano {} é bisiesto'.format(ano))
else:
    print('O ano {} não é bisiesto'.format(ano))