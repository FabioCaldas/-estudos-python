class ContaBancaria:
  def __init__(self, titular, saldo=0):
    self.titular = titular
    self.saldo = saldo
    self.ativa = True
 
  def depositar(self, valor):
    if not self.ativa:
      print("Conta inativa")
    elif valor == 0:
      print("Valor insuficiente para deposito")
    else:
      self.saldo += valor
      print(f"Deposito recebido de R${valor:.2f} com sucesso!")
 
  def sacar(self, valor):
    if not self.ativa:
      print("Conta inativa")
    elif valor > self.saldo:
      print("Saldo insuficiente")
    else:
      self.saldo -= valor
      print(f"Saque de R${valor:.2f} realizado com sucesso.")
 
  def fechar_conta(self):
    self.ativa = False
    print(f"A conta de {self.titular} foi encerrada com sucesso.")
 
  def __str__(self):
    return f"Titular: {self.titular} | Saldo: R${self.saldo} | Status: {self.ativa}"
  
# Exemplo de uso
conta1 = ContaBancaria("João", 1000)
print(conta1)
conta1.depositar(500)
conta1.sacar(200)
print(conta1)
conta1.fechar_conta()
conta1.depositar(100)
print(conta1)
