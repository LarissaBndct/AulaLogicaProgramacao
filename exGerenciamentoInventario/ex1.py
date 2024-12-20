import os 
limpaTela = lambda: os.system('cls')
limpaTela()

from entradaDados import inteiroPositivo, stringNaoVazia

##variaveis globais

nomeArquivo = "iventario.txt"

##implementação de funçoes

def menu():
    print("=========Menu de opçãoes==========")
    print("1. Adicionar produto ")
    print("2. Listar inventario ")
    print("3. Atualizar inventario ")
    print("4. Remover um produto ")
    print("5. Buscar um produto ")
    print("6. Sair ")

def adicionarProduto(nomeProduto, qtdProduto):
    try:
        with open(nomeArquivo, 'a') as arquivo: 
            arquivo.write(f"{nomeProduto}:{qtdProduto}\n")
            print(f"Produto {nomeProduto} foi adicionado com sucesso! ")
    except IOError:
        print("Erro: no acesso de abertura do arquivo:")
    except PermissionError:
        print("Erro: permissão de acesso ao arquivo ")
    except Exception as e:
        print(f"Erro: inesperado {e}")

def listarProdutos():
    try:
        with open(nomeArquivo, 'r') as arquivo:
            print(" ====== Inventário de produtos =====")
            print(f"{'produtos':<30} {'quantidade':<10}")
            for linha in arquivo: 
                produto, quantidade = linha.strip().split(":")
                print(f"{produto:<30} {quantidade:<10}")

    except IOError:
        print("Erro: no acesso de abertura do arquivo:")
    except PermissionError:
        print("Erro: permissão de acesso ao arquivo ")
    except FileNotFoundError:
        print("Erro: arquivo não encontrado ")
    except Exception as e:
        print(f"Erro: inesperado {e}")

def atualizarProduto(nomeProduto):
    try:
        with open(nomeArquivo, 'r') as arquivo:
            linhas = arquivo.readlines()

    except IOError:
        print("Erro: no acesso de abertura do arquivo:")
    except PermissionError:
        print("Erro: permissão de acesso ao arquivo ")
    except FileNotFoundError:
        print("Erro: arquivo não encontrado ")
    except Exception as e:
        print(f"Erro: inesperado {e}")
    
    try:
        with open(nomeArquivo, 'w') as arquivo:
            achouProduto = False
            for linha in linhas:
                if linha.startswith(f"{nomeProduto}"):
                    qtdProduto = inteiroPositivo("Digite a quantidade: ")
                    arquivo.write(f"{nomeProduto}:{qtdProduto}\n")
                    achouProduto = True
                else:
                    arquivo.write(linha)
            if achouProduto:
                print(f"Produto {nomeProduto} alterado com sucesso ")
            else:
                print("produto nao encontrado")

    except IOError:
        print("Erro: no acesso de abertura do arquivo:")
    except PermissionError:
        print("Erro: permissão de acesso ao arquivo ")
    except FileNotFoundError:
        print("Erro: arquivo não encontrado ")
    except Exception as e:
        print(f"Erro: inesperado {e}")

def removerProduto(nomeProduto):
    try:
        with open(nomeArquivo, 'r') as arquivo:
            linhas = arquivo.readlines()

    except IOError:
        print("Erro: no acesso de abertura do arquivo:")
    except PermissionError:
        print("Erro: permissão de acesso ao arquivo ")
    except FileNotFoundError:
        print("Erro: arquivo não encontrado ")
    except Exception as e:
        print(f"Erro: inesperado {e}")  
    
    try: 
        with open(nomeArquivo, 'w') as arquivo:
            achouProduto = False
            for linha in linhas:
                if linha.startswith(f"{nomeProduto}:"):
                    achouProduto = True
                else:
                    arquivo.write(linha)
            if achouProduto:
                print(f"Produto {nomeProduto} removido com sucesso")
            else:
                print(f"Produto {nomeProduto} não encontrado ")
    
    except IOError:
        print("Erro: no acesso de abertura do arquivo:")
    except PermissionError:
        print("Erro: permissão de acesso ao arquivo ")
    except FileNotFoundError:
        print("Erro: arquivo não encontrado ")
    except Exception as e:
        print(f"Erro: inesperado {e}") 

def buscarProduto(nomeProduto):
    try:
        with open(nomeArquivo, 'r') as arquivo:
            achouProduto = False
            
            print(f"{'produtos':<30} {'quantidade':<10}")
            for linha in arquivo: 
                produto, quantidade = linha.strip().split(":")
                if produto == nomeProduto:
                    print(" ====== Inventário de produtos =====")
                    print(f"{produto:<30} {quantidade:<10}")
                    return
            print(f"Produto {produto} não encontrado")
    except IOError:
        print("Erro: no acesso de abertura do arquivo:")
    except PermissionError:
        print("Erro: permissão de acesso ao arquivo ")
    except FileNotFoundError:
        print("Erro: arquivo não encontrado ")
    except Exception as e:
        print(f"Erro: inesperado {e}")
   

while True:
    limpaTela()
    menu()
    op = input("Digite a opção desejada: ")
    match op:
        case '1': ##adicionar produto
            nomeProduto = stringNaoVazia("Digite o nome do produto: ")
            qtdProduto = inteiroPositivo("Digite a quantidade: ")
            adicionarProduto(nomeProduto, qtdProduto)
            input("Enter para continuar ")
        case '2': ##listar produtos do inventario
            if os.path.getsize(nomeArquivo) > 0:
                listarProdutos()
            else:
                print("Inventário de produtos vazio!")
            input("Enter para continuar ")
        case '3':
            if os.path.getsize(nomeArquivo) > 0:
                nomeProduto = stringNaoVazia("Digite o nome do produto: ")
                atualizarProduto(nomeProduto)
            else:
                print("Inventário de produtos vazio!")
            input("Enter para continuar ")
        case '4':
            nomeProduto = input("Digite o nome do produto a ser removido: ")
            removerProduto(nomeProduto)
            input("Enter para continuar ")
        case '5':
            nomeProduto = input("Digite o nome do produto a ser buscado ")
            buscarProduto(nomeProduto)
            input("Enter para continuar ")
        case '6':
            limpaTela()
            break
        case _:
            print("opção inválida")