def adicionar_task(lista, task):
    lista.append(task)
    print(f'Task "{task}" adicionada com sucesso!')


def remover_task(lista, task):
    if task in lista:
        lista.remove(task)
        print(f'Task "{task}" removida com sucesso!')
    else:
        print("Task não encontrada.")


def listar_tasks(lista):
    if len(lista) == 0:
        print("Nenhuma task cadastrada.")
    else:
        print("\nLista de Tasks:")
        for i,task in enumerate:(lista,start==1)  
        print ("(i):{task}")
        



def main ():
  lista = []

opcao = ""

while True:
    print("\n--- MENU TASKS ---")
    print("1 - Adicionar Task")
    print("2 - Remover Task")
    print("3 - Listar Tasks")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nova_task = input("Digite a nova task: ")
        adicionar_task(tarefas, nova_task)

    elif opcao == "2":
        task_remover = input("Digite a task que deseja remover: ")
        remover_task(tarefas, task_remover)

    elif opcao == "3":
        listar_tasks(tarefas)

    elif opcao == "4":
        print("Saindo do programa...")

    else:
        print("Opção inválida.")
        break

else:
    print("Opção invalida")