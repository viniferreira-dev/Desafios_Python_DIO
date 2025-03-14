from abc import ABC, abstractmethod

class Conta:
    def __init__(self, saldo:float, numero:int,agencia:str,cliente:"Cliente",historico:"Historico"):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico
    
    def saldo(self):
        return self._saldo 
    
    @classmethod
    def nova_Conta(cls, cliente:"Cliente", numero:int):
        return cls(saldo=0.0, numero=numero, agencia="0001", cliente=Cliente, historico=Historico()) 
    
    def sacar(self, valor:float):
        return bool
    
    def depositar(self, valor:float):
        return bool
    
class ContaCorrente(Conta):
    
    def __init__(self, saldo, numero, agencia, cliente, historico, limite:float, limite_saques:int):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self.limite = limite
        self.limite_saques = limite_saques

class Historico:

    def __init__(self):
        pass

    def adicionar_transacao(self, transacao:"Transacao"):
        pass

class Transacao(ABC):

    @abstractmethod
    def registrar(self, conta:"Conta"):
        pass

class Deposito(Transacao):

    def __init__(self, valor:float):
        self.valor = valor

class Saque(Transacao):

    def __init__(self, valor:float):
        return conta.depositar(self.valor)

class Cliente:

    def __init__(self, endereco:str, contas:list):
        self.endereco = endereco
        self.contas = contas

    def realizar_transacao(self, conta: "Conta", transacao: "Transacao"):

        transacao.registrar(conta) 

class PessoaFisica(Cliente):

    def __init__(self, endereco, contas, cpf:str, nome:str, data_nascimento:str):
        super().__init__(endereco, contas)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

