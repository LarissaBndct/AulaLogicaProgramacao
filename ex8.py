import os
eletrodomesticos = []

while True:
    consumo = input("Informe o  consumo de energia em kWh de cada eletrodoméstico ou digite 's' para sair ")
    if consumo == 's' or consumo == 'S':
        os.system("cls")
        break
    else:
        if "" == consumo:
            print("Informe um valor válido")
        else:
            eletrodomesticos.append(consumo)

soma = sum(eletrodomesticos)
print(f"Cosumo total sem tarifa: {soma}")
# To do:
#5.Aplicar a tarifa de acordo com o consumo total:
#-Se o consumo for até 100 kWh, a tarifa é de R$0,50 por kWh.
#-Se o consumo for entre 101 e 200 kWh, a tarifa é de R$0,75 por kWh.
#-Se o consumo for acima de 200 kWh, a tarifa é de R$1,00 por kWh.
#6.Exibir o consumo total e o valor a ser pago.