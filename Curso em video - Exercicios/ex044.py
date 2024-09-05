print('{:=^40}'.format('MaxTitanio'))
valor=float(input('Preço da compra: R$'))
pg=int(input('''FORMA DE PAGAMENTO
=================================
[ 1 ] À vista no dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] Em até 3x ou mais no cartão
=================================
Qual forma de pagamento? '''))
if pg==1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor,valor*0.9))
elif pg==2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor,valor*0.95))
elif pg==3:
    print('Sua compra vai se manter o valor R${:.2f} e o valor das parcelas fica em R${:.2f}.'.format(valor,valor/2))
elif pg==4:
    qparcelas=int(input('Quantas parcelas? '))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final e o valor das parcelas fica em R${:.2f}.'.format(valor,(valor*1.20),valor/qparcelas))
else:
    print('\033[1;31mOPÇÃO INVALIDA\033[m.\nPor gentileza, digitar opções existentes.')
