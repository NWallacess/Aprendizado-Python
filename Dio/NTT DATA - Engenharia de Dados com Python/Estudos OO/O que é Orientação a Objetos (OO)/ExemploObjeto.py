class cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("Auau!!")

    def dormir(self):
        self.acordado = False
        print("Zzzzz...")


dog_1 = cachorro("Rex", 'verde',False)
dog_2 = cachorro('Pipoca','Branco',)

dog_1.latir()