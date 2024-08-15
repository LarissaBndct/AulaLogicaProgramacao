import os,random

print("~~~~~~~~~~Adivinhe o número secreto~~~~~~~~~~~~")

numAleatrio = random.randint(1,50) #escolhendo um numero aleatrio de 1 a 50
tentativas = 0


while True:
    num = input("Digite um número ou 'S' para sair\n")
    tentativas +=1
    if num == 'S' or num == 's':
        os.system("cls")
        break
    num = int(num)
    
    if(num > numAleatrio):
        print("O número aletório é menor!")
    elif(num < numAleatrio):
        print("o número aleatório é maior!")
    elif(num == numAleatrio):
        print(f"Parabéns, você acertou o numero secreto em {tentativas} tentativas")

