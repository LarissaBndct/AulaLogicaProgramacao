import os

def CalculoMedia(prova1, prova2):
    m = (prova1 + prova2)/2
    if m < 2:
        print(f"Média {m:.2f}, situação: reprovado")
    elif m >= 2 and m < 6:
        print(f"Média: {m:.2f}, situação: necessário realizar prova substutiva")
    elif m >= 6:
        print(f"Média: {m:.2f}, situação: aprovado")

while True:


    p1 = float(input("Insira a nota da primeira prova "))
    p2 = float(input("Insira a nota da segunda prova "))
    media  = CalculoMedia(p1,p2)
    selecao = input("Digite 's' para sair ou qualquer tecla para continuar ")
    if selecao == 's' or selecao == 'S':
        os.system("cls")
        break
