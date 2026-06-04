def adicionar_item(lista, item):
  lista.append(item)
  print("Item adicionado com sucesso.")
 
def remover_item(lista, item):
  if item in lista:
    lista.remove(item)
    print("Item removido!")
  else:
    print("Item nao encontrado!")
 
def listar_item(lista):
  if len(lista) == 0:
    print("Lista vazia.")
  else:
    print("\nLista de itens:")
    for i, item in enumerate(lista, start=1):
      print(f"{i}: {item}")
 
def programa_principal():
  lista = []
 
  while True:
    print("\n --- Lista de compras ---")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Listar itens")
    print("4 - Sair")
 
    opcao = input("Escolha uma opção: ").lower()
 
    if opcao == '1':
      item = input("Digite o item: ")
      adicionar_item(lista, item)
 
    elif opcao == '2':
      item = input("Digite o item a ser removido: ")
      remover_item(lista, item)
 
    elif opcao == '3':
      listar_item(lista)
 
    elif opcao == '4':
      print("Saindo")
      break
    else:
      print("Opção inválida, tente novamente!")
 
 
programa principal()