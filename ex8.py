import os
eletrodomesticos = []
tarifa = 0
while True:
    consumo = input("Informe o  consumo de energia em kWh de cada eletrodoméstico ou digite 's' para sair ")
    if consumo == 's' or consumo == 'S':
        os.system("cls")
        break
    else:
        if "" == consumo:
            print("Informe um valor válido")
        else:
            consumo = float(consumo)
            eletrodomesticos.append(consumo)

somaConsumo = sum(eletrodomesticos)
if somaConsumo <= 100:
    tarifa = somaConsumo * 0.5
elif somaConsumo <= 200:
    tarifa = somaConsumo * 0.75
elif somaConsumo > 200:
    tarifa = somaConsumo 
print(f"Consumo total: {somaConsumo}kWh. Total a pagar: R${tarifa:.2f}")
