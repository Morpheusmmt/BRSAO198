"""
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

print ("Digite a temperatura que deseja converter:")
temp = float(input())
print("Digite a unidade de origem (C para Celsius, F para Fahrenheit, K para Kelvin):")
origem = input().upper()
print("Digite a unidade de destino (C para Celsius, F para Fahrenheit, K para Kelvin):")
destino = input().upper()

if origem == destino:
    print(f"A temperatura já está na unidade desejada: {temp}{origem}")

elif origem == "C":
    if destino == "F":
        convertido = (temp * 9/5) + 32
        print(f"{temp}°C é igual a {convertido:.2f}°F")
    elif destino == "K":
        convertido = temp + 273.15
        print(f"{temp}°C é igual a {convertido:.2f}K")
    else:
        print("Unidade de destino inválida.")

elif origem == "F":
    if destino == "C":
        convertido = (temp - 32) * 5/9
        print(f"{temp}°F é igual a {convertido:.2f}°C")
    elif destino == "K":
        convertido = (temp - 32) * 5/9 + 273.15
        print(f"{temp}°F é igual a {convertido:.2f}K")
    else:
        print("Unidade de destino inválida.")

elif origem == "K":
    if destino == "C":
        convertido = temp - 273.15
        print(f"{temp}K é igual a {convertido:.2f}°C")
    elif destino == "F":
        convertido = (temp - 273.15) * 9/5 + 32
        print(f"{temp}K é igual a {convertido:.2f}°F")
    else:
        print("Unidade de destino inválida.")
        
else:
    print("Unidade de origem inválida.")