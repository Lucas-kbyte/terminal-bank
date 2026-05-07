from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, taxa_operacao = 1.0):
        super().__init__(numero, cliente)
        self.taxa_operacao = taxa_operacao
        ## ta dando merda em tudo