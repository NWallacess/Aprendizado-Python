valor_da_casa=float(input('Qual é o valor da casa? R$'))
salario=float(input('Quanto você recebe? R$'))
tempo=int(input('Em quantos anos você pretende pagar? '))
parcelas=tempo*12
salario30p=salario*0.30
prestacao=valor_da_casa/parcelas
print('O valor das prestações mensais é \033[1;31mR${:.2f}\033[m'.format(prestacao))
if salario30p >= prestacao:
    print('\033[1;32mEMPRESTIMO APROVADO\033[m \nÉ possivel realizar a compra da casa')
else:
    print('\033[1;31mEMPRESTIMO NEGADO\033[m \nInfelizmente não é possivel comprar essa casa.')