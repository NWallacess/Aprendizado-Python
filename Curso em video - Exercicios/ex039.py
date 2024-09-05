from datetime import date
ano = int(input('Qua ano voce nasceu?'))
sexo = input('Qual é o seu sexo? FEMENINO OU MASCULINO:').upper().strip()
ano_de_hoje= date.today().year
idade = ano_de_hoje - ano
alistamento=ano+18
print('Quem nasceu em {} tem {} anos em {}.'.format(ano,idade,ano_de_hoje))
if sexo == 'FEMININO':
    print('''Seu sexo é FEMININO.
No Brasil. Mulheres não tem a obrigação de realizar o alistamento.''')
elif ano_de_hoje < alistamento:
    print('''Ainda falta {} ano(s) para o seu alistamento.
Seu alistamento sera em {}.'''.format((alistamento-ano_de_hoje),alistamento))
elif idade == alistamento:
    print('Você já fez 18 anos esse ano.\nEntão você tem que se alistar esse ano.\nRealize \033[1;31mIMEDIATAMENTE\033[m')
else:
    print('''Seu alistamente já passou, foi em {}.
Caso ainda não tenha se alistado, busque uma Junta militar para realizar o alistamento.'''.format(alistamento))
