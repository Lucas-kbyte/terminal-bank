from conta import Conta

class Juros(Conta):
    def __init__(self, numero, cliente, juros = 1.01):
        super().__init__(numero, cliente)
        self.juros = juros
    
    def sacar(self, valor):
        if valor <= self.__saldo:            
            self.__saldo -= valor
            print(f"Saque de R$ {valor} Feito com sucesso")
        else:
            print("Saque cancelado, favor tente novamente com um número valido")
