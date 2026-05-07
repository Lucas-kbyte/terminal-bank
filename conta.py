class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.__saldo = 0.0

    def get_saldo(self):
        return self.__saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor} feito com sucesso")
    
    def adicionar_saldo(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Sucesso! R$ {valor} adicionados.")
        else:
            print("Erro: O valor deve ser positivo!")
        ## Eu fiz funciona as modificações
        ## eu menti, tiv que trca de lugar sacar
