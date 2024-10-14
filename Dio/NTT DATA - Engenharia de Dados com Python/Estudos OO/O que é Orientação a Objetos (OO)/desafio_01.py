class Bicicleta:
    def __init__(self,cor,modelo,ano,valor):
        self.cor = cor          #Atributos da classe
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("plin, plin...")
    def parar(self):
        print("Parando....")
        print("Parou")

    def correr(self):
        print("Vrummmm")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

caloi = Bicicleta("Amerela", "Caloi", 2024, 250)
caloi.buzinar()

print(caloi)