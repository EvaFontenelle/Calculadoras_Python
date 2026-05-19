from calculadoras.calculoCTFC import calcularCTFC

print("Calculadora de fahrenheit para celsius:")

fahrenheit = float(input("Digite a temperatura em fahrenhait e tecle ENTER:"))
celsius = calcularCTFC(fahrenheit)

print(f"{fahrenheit}°F = {celsius:.2f}°C")