import os
nota1 = float(input("Insira a primeira nota "))
peso1 = float(input("Insira o peso da primeira nota "))
nota2 = float(input("Insira a segunda nota "))
peso2 = float(input("Insira o peso da segunda nota "))
nota3 = float(input("Insira a terceira nota "))
peso3 = float(input("Insira o peso da terceira nota "))

# media ponderada: n1 * p1 + n2 * p2 + n3 * p3 / p1 + p2 + p3 

mediaPonderada = ((nota1 * peso1) + (nota2 * peso2) + ( nota3 * peso3)) / (peso1 + peso2 + peso3)

print(f"A media ponderada é de: {mediaPonderada:.2f}")

os.system('cls')