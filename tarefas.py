tarefas = []
while True:
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")
    elif opcao == "2":
        print("Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")   