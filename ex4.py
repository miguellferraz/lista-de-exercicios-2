from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    def __init__(self, numero_conta, titular, saldo=0.0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def calcular_saldo(self):
        pass

    def exibir_informacoes(self):
        return (f"Conta: {self.numero_conta}\n"
                f"Titular: {self.titular}\n"
                f"Saldo: R$ {self.saldo:.2f}")

class ContaCorrente(ContaBancaria):
    def __init__(self, numero_conta, titular, saldo=0.0, limite_cheque_especial=500.0):
        super().__init__(numero_conta, titular, saldo)
        self.limite_cheque_especial = limite_cheque_especial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and (self.saldo - valor >= -self.limite_cheque_especial):
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para saque ou valor inválido.")

    def calcular_saldo(self):
        return self.saldo

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_conta, titular, saldo=0.0, taxa_juros=0.02):
        super().__init__(numero_conta, titular, saldo)
        self.taxa_juros = taxa_juros

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para saque ou valor inválido.")

    def calcular_saldo(self):
        self.saldo += self.saldo * self.taxa_juros
        return self.saldo

conta_corrente = ContaCorrente(numero_conta="652130", titular="Lamiz", saldo=100.0)
print(conta_corrente.exibir_informacoes())
conta_corrente.depositar(200)
conta_corrente.sacar(400)  
print(conta_corrente.exibir_informacoes())

conta_poupanca = ContaPoupanca(numero_conta="983483", titular="Zago", saldo=500.0)
print(conta_poupanca.exibir_informacoes())
conta_poupanca.depositar(100)
conta_poupanca.sacar(700)  
conta_poupanca.calcular_saldo()  
print(conta_poupanca.exibir_informacoes())
