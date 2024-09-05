#Rotinas.
def voto(ano_de_nasc):
    from datetime import date
    dic = {'idade': 0, 'vota': ''}
    ano_atual = date.today().year()
    dic['idade'] = ano_atual - ano_de_nasc
    if dic['idade'] >= 60:
        dic['vota']= 'VOTO OPICIONAL'  
        return f'Com {dic["idade"]} anos: {dic["vota"]}'
    elif dic['idade'] >=18:
        dic ['vota'] = 'VOTO OBRIGATORIO'
        return f'Com {dic["idade"]} anos: {dic["vota"]}'
    elif dic['idade']>=16:
        dic['vota'] = 'VOTO OPICIONAL'
        return f'Com {dic["idade"]} anos: {dic["vota"]}'
    else:
        dic['vota'] = 'NÃO VOTA'
        return f'Com {dic["idade"]} anos: {dic["vota"]}'
        



#Codigo principal.
print('--'*20)
nascimente=int(input('Em que ano você nasceu: '))
print(voto(nascimente))