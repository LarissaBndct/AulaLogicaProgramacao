import os

while True:
    numero = int(input("Digite o numero para visualizar a tabuada "))

    for n in range(11):
        tabuada = n * numero

        print(f"{n} x {numero} = {tabuada}")
    
    op = input("Digite s para sair ou aperte qualquer tecla para continuar ")
    if op == "s" or op == "S":
        os.system("cls")
        break



