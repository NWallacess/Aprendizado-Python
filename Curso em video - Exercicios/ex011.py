altura=float(input('Qual é a altura da pareda(em metros)?'))
largura=float(input('Qual é a largura da parede(em metros)?'))
area=altura*largura
arealintada=(area)/2
print('Sua parede tem dimesão {}x{} e sua área é de {}m².'.format(altura,largura,area))
print('Para pintar essa parede é necessario {}litros de tinta.'.format(arealintada))