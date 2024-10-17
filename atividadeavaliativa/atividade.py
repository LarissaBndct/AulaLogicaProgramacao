import os

pacientes = []
atendidos = []
codigo = 0

def menu():
    print("\nSelecione a opção desejada")
    print("1. Adicionar paciente à lista de espera")
    print("2. Remover paciente da lista de espera")
    print("3. Exibir lista de pacientes atendidos")
    print("4. Exibir lista de espera")
    print("5. Sair")

def adicionarPaciente(pacientes, paciente, especialidade):
    codigo = len(pacientes) + 1
    pacientes.append([codigo, paciente, especialidade])
    print(f"Paciente {paciente} adicionado com sucesso!!")

def PacientesEspera(pacientes):
    print("========== Lista de Espera ==========")
    for item in pacientes:
        print(f"{item[0]}. {item[1]}. {item[2]}")

def removerPacienteListaEspera(pacientes, atendidos, codigo):
    for item in pacientes:
        if item[0] == codigo:
            print(f"Paciente {item[1]} removido da lista de espera")
            atendidos.append([len(atendidos) + 1, item[1], item[2]])
            pacientes.remove(item)
            return
    print("Paciente não encontrado")

def listaAtendidos(atendidos):
    print("========== Pacientes Atendidos ==========")
    for item in atendidos:
        print(f"{item[0]}. {item[1]}. {item[2]}")

while True:
    menu()
    op = input("Digite a opção desejada (1 - 5): ").strip()
    
    if op == '1':
        paciente = input("Informe o nome do paciente: ").strip()
        especialidade = input("Informe a especialidade: ").strip()
        if paciente and especialidade:
            adicionarPaciente(pacientes, paciente, especialidade)
        else:
            print("Nenhuma das informações deve estar vazia.")
    
    elif op == '2':
        if pacientes:
            PacientesEspera(pacientes)
            codigo = int(input("Digite o código do paciente a ser removido: ").strip())
            removerPacienteListaEspera(pacientes, atendidos, codigo)
        else:
            print("Lista vazia.")
    
    elif op == '3':
        if atendidos:
            listaAtendidos(atendidos)
        else:
            print("Lista vazia.")
    
    elif op == '4':
        if pacientes:
            PacientesEspera(pacientes)
        else:
            print("Lista vazia.")
    
    elif op == '5':
        os.system('cls')
        break
    
    else:
        print("Opção inválida!")
