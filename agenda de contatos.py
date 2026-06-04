def adicionar_contato(agenda, nome, telefone):
    agenda[nome] = telefone
    print(f"Contato '{nome}' adicionado com sucesso!")


def remover_contato(agenda, nome):
    if nome in agenda:
        del agenda[nome]
        print(f"Contato '{nome}' removido com sucesso!")
    else:
        print( "não encontrado.")



def buscar_contato(agenda, nome):
    if nome in agenda:
        print(f"Telefone de {nome}: {agenda[nome]}")
    else:
        print("não encontrado.")


def listar_contatos(agenda):
    if len(agenda) == 0:
        print("sem contatos.")
    else:
        print("\n--- Lista de Contatos ---")
        for nome, telefone in agenda.items():
            print(f"{nome}: {telefone}")


agenda = {}

while True:
    print("\n=== AGENDA DE CONTATOS ===")
    print("1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Buscar contato")
    print("4 - Listar contatos")
    print("s - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        adicionar_contato(agenda, nome, telefone)

    elif opcao == "2":
        nome = input("Digite o nome do contato a remover: ")
        remover_contato(agenda, nome)

    elif opcao == "3":
        nome = input("Digite o nome do contato a buscar: ")
        buscar_contato(agenda, nome)

    elif opcao == "4":
        listar_contatos(agenda)

    elif opcao.lower() == "s":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")