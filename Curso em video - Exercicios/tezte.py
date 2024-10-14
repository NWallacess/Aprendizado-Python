def analise_vendas(vendas):
    # TODO: Calcule o total de vendas e realize a média mensal:
    total_vendas=0
    for l in vendas:
        total_vendas+=l
    
    media_vendas = total_vendas/len(vendas)

    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de inteiros:
    entrada.split(',')
    vendas = list()
    vendas.append(map(int,entrada))
    
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))