import math

def AreaDoCirculo(raio):
    a = math.pi * (raio**2)

    return a

r = float(input("Insira a area do circulo "))

area = AreaDoCirculo(r)

print(f"A area do circilo de raio {r:.2f} é de: {area:.2f}")