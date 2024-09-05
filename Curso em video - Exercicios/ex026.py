frase=input('Digite uma frase: ').upper().strip()
print('Sua frase tem {} letras a'.format(frase.lower().count("a")))
print('A primeira aparição é na posição {}'.format((frase.find('a'))+1))
print('A Ultima aparição do a é na posição {}'.format(frase.rfind('a')+1))