from abc import ABC, abstractmethod

class controleRemoto(ABC):
    
    @abstractmethod
    def ligar(self):
        pass

    def desligar(self):
        pass

class controleTv(controleRemoto):
    def ligar(self):
        print("Ligando a Tv...")
        print("Ligado")
    
    def desligar(self):
        print("desligando a Tv...")
        print("Desligado")

class ControleAr(controleRemoto):
    def ligar(self):
        print("Ligando a Ar...")
        print("Ligado")
    
    def desligar(self):
        print("desligando a AR...")
        print("Desligado")

controle = controleTv()
controle.ligar()
controle.desligar()