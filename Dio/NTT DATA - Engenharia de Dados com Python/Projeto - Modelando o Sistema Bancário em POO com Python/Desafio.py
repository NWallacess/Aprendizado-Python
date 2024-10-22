#Criando Clas
from abc import ABC,abstractmethod
from datetime import datetime

class Cliente():
    def __init__(self,end:str):
        super().__init__
        self.endereco = end
        self.conta = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def Criar_conta(self,Conta):
        self.conta.append(Conta)

class PessoaFisica(Cliente):
    def __init__(self,CPF,Nome,data_nasc, end):
        super().__init__(end)
        self.cpf = CPF
        self.nome = Nome
        self.data_nasc = data_nasc

class Conta:
    def __init__(self,numero:int,cliente:Cliente,):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._agencia

    @property
    def historico(self):
        return self._historico

    def Sacar(self, valor):
        saldo = self.saldo
        execedeu_saldo = valor > saldo
        
        if execedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente @@@")

        elif valor> 0 :
            self.saldo-=valor
            print("\n ###Saque realidado com sucesso!###")
            return True
        
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            
        return False

    def Depositar(self, valor):
        if valor > 0:
            self.saldo+=valor
            print("\n ###Deposito realidado com sucesso!###")
        
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True

class ContaCorrente(Conta):
    def __init__(self,numero,cliente,):
        super().__init__(numero, cliente)
        self.limite = 500
        self.limite_saque = 3

    def Sacar(self, valor):
        numero_saque = len([transacao for transacao in self.historico._transacoes if transacao["Tipo"] == Sacar.__name__])
    
        execedeu = valor > self.limite
        execedeuSaque = numero_saque > self.limite_saque

        if execedeu:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente @@@")
        elif execedeuSaque:
            print("\n@@@ Operação falhou! Você ultrapassou o limite diario @@@")
        else:
            return super().Sacar(valor)
        return False

    def __str__(self):
        return f"Agencia:\t{self.agencia}\nC\C:\t\t{self.numero}\nTitular:\t{self._cliente.nome}"

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionarTransacao(self, transacao):
        self._transacoes.append({
            "tipo":transacao.__class__.__name__,
            "valor":transacao.valor,
            "data":datetime.now()
        })

class Transacao(ABC):
    
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self, conta):
        pass

class Depositar(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self.valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
        
class Sacar(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self.valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
        