from conta import Conta
from renderjuros import Juros
from cliente import Cliente
from contacorrente import ContaCorrente

import time
import os

def inicio():
    print("=" * 45)
    print("Identificação do Cliente")
    
    nome = input("Digite seu nome: ")
    cpf_input = input("Digite seu CPF: ") 
    
    cliente1 = Cliente(nome, cpf_input)
    
    print("=" * 45)
    print(f"Cliente {cliente1.nome} cadastrado com sucesso!")
    
    print(f"CPF registrado: {cliente1.get_cpf()}") 
    
    time.sleep(5)


def menu():


    while True:
        usuario_conta = Conta(0)

        inicio()

        print("=" * 45)
        print("—————————————— Banco Sp4mton ——————————————")
        print("1 - Ver saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Transfererir")
        print("5 - Sair")
        print("=" * 45)
        opcao = int(input("Digite sua opção"))
        
        match opcao:
            case "1":
                print(f"Saldo atual: R$ {minha_conta.get_saldo()}")

            case "2":
                print("Quanto você gostaria de depositar?")
                try:
                        quantia = float(input("Quanto você deseja depositar? "))
        
                        minha_conta.adicionar_saldo(quantia)
        
                        print(f"Novo saldo total: R$ {minha_conta.get_saldo()}")
        
                except ValueError:
                        print("Por favor, digite apenas números!")
                
            case "3":
                pass

            case "4":
                pass

            case "5":
                pass
        
inicio()