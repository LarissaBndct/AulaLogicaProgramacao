import os
print(f'{"Calculadora":~^60}')

while True:
    operacao = input("Escolha a operação adição = +, subtração = -,multiplicação = * e divisão = / \n(ou digite qualquer tecla para sair)\n")
    ehOperacao = operacao == "+" or operacao == "-" or operacao == "*" or operacao == "/"   
    if(ehOperacao == False): 
        os.system("cls")
        break
    op1 = float(input("Digite o primerio número da operação "))
    op2 = float(input("Digite o segundo número da operação "))
    resultado = 0
    if operacao == "+":
        resultado = op1 + op2
    elif operacao == "-":
        resultado = op1 - op2
    elif operacao == "*":
        resultado = op1 * op2
    elif(operacao == "/"):
        resultado = op1 / op2
    print(f" {op1} {operacao} {op2} = {resultado} ")
    