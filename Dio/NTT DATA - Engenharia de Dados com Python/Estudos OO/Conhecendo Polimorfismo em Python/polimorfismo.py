class Passaro:
    def voar(self):
        print("Voandoo.....")

class Pardal(Passaro):
    def voar(self):
        super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

# Exemplo ruim de uso de herança para "ganhar" o metodo voar
class Avião(Passaro):
    def voar(self):
        print("Avião esta decolando!!!")

def plano_voo(obj):
    obj.voar()

p1 = Pardal()
p2 = Avestruz()
p3 = Avião()

plano_voo(p1)
plano_voo(p2)
plano_voo(p3)