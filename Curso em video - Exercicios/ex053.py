text=input('Digite um frase: ').strip().upper().split()
text2=(''.join(text))
inverso= ''
for letra in range(len(text2)-1,-1,-1):
    inverso += text2[letra]
print('A frase {} ao contrario é igual a {}'.format(text2,inverso))
if inverso == text2:
    print('Temos um palintromo!')
else:
    print('Não é um palindromo.')