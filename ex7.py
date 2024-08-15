import os

saldo = 0

def depositar(valorDep):

    global saldo
    saldo += valorDep 

    return print(f"Deposito de R${valorDep:.2f} realizado com sucesso! Novo saldo: R${saldo:.2f}")

def Sacar(valorSaq):
    global saldo
    if(valorSaq > saldo):
        print("Saldo insuficiente")
    else:

        saldo -= valorSaq
        print(f"Saque realizado com sucesso! Novo saldo: R${saldo:.2f}")

while True:
    operacao = input("digite 's' para sacar, 'd' para depositar ou 'v para visualizar saldo'\n(ou tecle 'enter' para sair) ")
    ehOperacao = operacao == 's' or operacao == 'S' or  operacao == 'd'or  operacao == 'D'  or operacao =="v" or  operacao == 'V'
    if(ehOperacao == False):
        os.system("cls")
        break
    if(operacao == 's' or operacao == 'S'):
        vSaque = float(input("Digite o valor para o saque: "))
        Sacar(vSaque)

    elif(operacao == 'd'or operacao == 'S'):
        vDeposito = float(input("Digite o valor para o depósito: "))
        depositar(vDeposito)

    elif(operacao == 'v' or operacao == 'V'):
        print(f"saldo da conta = R${saldo:.2f}")
