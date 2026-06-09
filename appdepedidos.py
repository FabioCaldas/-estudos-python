class Pedido:
  def __init__(self, numero, cliente):
    self.numero = numero
    self.cliente = cliente
    self.itens = []
    self.status = "Aberto"
 
  def adicionar_item(self, item, preco):
    self.itens.append({"item": item, "preco": preco})
    print(f"Item: {item} adicionado ao pedido {self.numero}")
 
  def calcular_total(self):
    total = 0
    for item, preco in self.itens:
      total += item["preco"]
      return total
 
  def atualizar_status(self, novo_status):
    self.status = novo_status
    print(f"Status do pedido {self.pedido} atualizado para {self.status}")
 
  def __str__(self):
    lista_itens = ""
   
    for item, preco in self.itens:
      lista_itens += f"- {item}: R${preco:.2f}\n"
 
    return(
        f"Pedido: {self.numero}\n"
        f"Cliente: {self.cliente}\n"
        f"Status: {self.status}\n"
        f"Itens: \n{lista_itens}"
        f"Total: R${self.calcular_total():.2f}"
    )