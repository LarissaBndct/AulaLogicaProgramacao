import os
listaTarefas = []
tarefas = []
status = False

def Menu():
    print("Selecione a opção desejada: ")
    print("1 - Adicionar tarefa \n2 - Remover tarefa \n3 - Listar Todas as tarefas \n4 - Marcar tarefa como realizada \n5 - listar tarefas realizadas \n6 Listar tarefas não realizadas \n7 - Sair")

def AdicionarTarefa():
    while True:
        tarefa = input ("Informe a tarefa ou tecle 'v' para listar tarefas: ")
        if tarefa == "":
            print("informe uma tarefa")
        elif tarefa == 'v' or tarefa == 'V':
            ListarTodasTarefas()
        else:
            tarefas.append(tarefa)
            tarefas.append(status)
            listaTarefas.append(tarefas)
            print(f"tarefa: {tarefa} adicionada com sucesso!")

def ConversaoStatus(status):
    if status == True:
        situacaoStatus = "Realizada"
    else:
        situacaoStatus = "Não realizada"
    return situacaoStatus

def RemoverTarefa():
    return print("Tarefa removida com sucesso")

def ListarTodasTarefas():
    for item in tarefas:
        print(f"{item}")
     

def ProgramaPrincipal():
    print("======Lista de tarefas======")
    while True:
        Menu()
        opcao = int(input())

        if opcao == 1:
            AdicionarTarefa()
        elif opcao == 2:
            RemoverTarefa()
        elif opcao == 3:
            ListarTodasTarefas()
        elif opcao == 7:
            os.system('cls')
            break

ProgramaPrincipal()
