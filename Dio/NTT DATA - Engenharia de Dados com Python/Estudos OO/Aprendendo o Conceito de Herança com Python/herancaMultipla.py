class animal():
    def __init__(self, num_patas):
        self.num_patas = num_patas
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


class aveis(animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico


class mamiferos(animal):
    def __init__(self,cor_pelo,**kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo

class cachorro(mamiferos):
    pass

class gato(mamiferos):
    pass

class leao(mamiferos):
    pass

class ornitorrinco(mamiferos,aveis):
    def __init__(self, cor_pelo, num_patas, cor_bico):
        print(ornitorrinco.__mro__)
        super().__init__(cor_pelo = cor_pelo,num_patas=num_patas,cor_bico=cor_bico)

Cat = gato(num_patas=4,cor_pelo="preto")
Perry = ornitorrinco(num_patas = 4,cor_pelo="Verde",cor_bico ="Laranja")

print(Cat)
print(Perry)