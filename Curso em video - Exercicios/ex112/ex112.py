from utilidadecuv import moeda,dados


preco = input('Digite um valor: R$ ')
preco = dados.validador(preco)
moeda.resumo(preco,10,10)