import os
os.system('cls')

### Implementação das funções ###

def menu():
    print("\nMenu de Opções")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3.Listar todas as tarefas")
    print("4.Marcar tarefa como realizada")
    print("5.Listar tarefas realizadas")
    print("6.Listar tarefas não realizadas")
    print("7.Sair")

def adicionar_tarefa(lista_tarefas,tarefa):
    lista_tarefas.append([tarefa,False])
    print(f"Tarefa {tarefa} adicionada com sucesso!!")

def listar_tarefas(lista_tarefas):
    print("### Lista de tarefas ###")
    for i,item in enumerate(lista_tarefas,1):
        if item[1] == True:
            status = "realizada"
        else:
            status = "Não realizada"
        print(f"{i}.{item[0]: <20} - {status: <20}")        


def remover_tarefa(lista_tarefas,tarefa):
    for item in lista_tarefas:
        if item[0] == tarefa:
            lista_tarefas.remove(item)
            print(f"Tarefa {tarefa} removida com sucesso !!")
            return
    print(f"Tarefa {tarefa} não encontrada !!!")

def marcar_tarefa(lista_tarefas,tarefa):
    for item in lista_tarefas:
        if item[0] == tarefa:
            if item[1] == True:
                print(f"Tarefa {tarefa} já foi realizada !!")
            else:
                item[1] = True
                print(f"Tarefa {tarefa} foi marcada com sucesso !!")
            return
    print(f"Tarefa {tarefa} não encontrada !!")

def listar_tarefas_filtradas(lista_tarefas,sit):
    lista_filtrada = []
    for item in lista_tarefas:
        if item[1] == sit:
            lista_filtrada.append(item)    
    if sit == True:
        print("### Lista de tarefas realizadas ###")
    else:
        print("### Lista de tarefas não realizadas ###")
    for i,item in enumerate(lista_filtrada,1):
        print(f"{i}.{item[0]}")



### Programa Principal ###

lista_tarefas = []
while True:
    menu()
    op = input("Digite a opção desejada (1 - 7): ")
    if op == '1': #adicionar a tarefa
     while True:
        tarefa = input("Digite a tarefa a ser inserida : ").strip() 
        if tarefa != "":       
            adicionar_tarefa(lista_tarefas,tarefa)
            break
        else:
            print("Tarefa inválida !!!")
      
    elif op == '2': #remover uma determinda tarefa
        if lista_tarefas:
            listar_tarefas(lista_tarefas)
            tarefa = input("Digite a tarefa a ser removida : ").strip()
            remover_tarefa(lista_tarefas,tarefa)
        else:
            print("Lista de tarefas vazia !!")
    elif op == '3': #listar todas as tarefas
        if lista_tarefas:
            listar_tarefas(lista_tarefas)
        else:
            print("Lista de tarefas vazia !!")
    elif op == '4': #marcar tarefa realizada
        if lista_tarefas:
            tarefa = input("Digite a tarefa a ser marcada : ").strip()
            marcar_tarefa(lista_tarefas,tarefa)
        else:
            print("Lista de tarefas vazia !!")
    elif op == '5': #listar tarefas realizadas
        if lista_tarefas:
            listar_tarefas_filtradas(lista_tarefas,True)
        else:
            print("Lista de tarefas vazia !!")
    elif op == '6': #listar tarefas não realizadas
        if lista_tarefas:
            listar_tarefas_filtradas(lista_tarefas,False)
        else:
            print("Lista de tarefas vazia !!")
    elif op == '7': #sair do programa
        os.system('cls')
        break
    else:
        print("Opção inválida, tente novamente !!!")

