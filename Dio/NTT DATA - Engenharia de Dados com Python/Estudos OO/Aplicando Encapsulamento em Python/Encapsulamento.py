class conta:    
    def __init__(self,saldo=0, numAgencia=''):
        self._saldo = saldo
        self.numAgencia = numAgencia

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo += valor

    def mostrarSaldo(self):
        return self._saldo


contacc= conta(100,"0010")

print(contacc._saldo)