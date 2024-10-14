class Pessoa:
    def __init__(self, nome, anoNasc):
        self._nome = nome
        self._anoNasc = anoNasc

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._anoNasc
    
pessoa = Pessoa("maria", 1999)
print(f'nome: {pessoa.nome}, idade: {pessoa.idade}')