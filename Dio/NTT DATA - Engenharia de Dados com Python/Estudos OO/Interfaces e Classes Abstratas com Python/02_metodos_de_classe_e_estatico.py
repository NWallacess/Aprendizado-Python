class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_apariti_data_nasc(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_de_idade(idade):
        return idade >= 18


p = Pessoa("Maria", 20)
print(p.nome, p.idade)

p2 = Pessoa.criar_apariti_data_nasc(1999, 3, 21, "guilherme")
print(p2.nome, p2.idade)

print(Pessoa.e_maior_de_idade(18),
Pessoa.e_maior_de_idade(8),
Pessoa.e_maior_de_idade(28))