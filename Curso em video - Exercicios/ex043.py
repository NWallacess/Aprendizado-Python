peso=float(input('Qual é seu peso? (Kg)'))
altura=float(input('Qual é sua altura? (Cm)' ))
alturam=altura/100
imc=peso/alturam**2
print('Seu Indice de Massa Corporal(IMC) é {:.2f}'.format(imc))
if imc <18:
    print('Classificação: Abaixo do peso.')
elif imc<25:
    print('Classificação: Peso ideal.')
elif imc<30:
    print('Classificação: Sobrepeso')
elif imc < 40:
    print('Classificação: Obessidade.')
else:
    print('Classificação: Obessidade Mórbida')