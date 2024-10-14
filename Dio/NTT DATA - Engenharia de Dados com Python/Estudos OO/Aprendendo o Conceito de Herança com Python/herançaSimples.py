class veiculo():
    def __init__(self, cor,placa,numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando motor.....")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(veiculo):
    pass

class Carro(veiculo):
    pass

class Caminhao(veiculo):
    def __init__(self,cor,placa,numero_rodas, carregado=False):
        super().__init__(cor,placa,numero_rodas)
        self.carregado = carregado

    def Esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'}, esta carregado")
    

moto = Motocicleta("preta","abc1234",2)
carro = Carro("cinza","lsd6969",4)
Otimosprime = Caminhao("vermelho com azul", "otimos222",6,True)

print(moto)
print(carro)
print(Otimosprime)
