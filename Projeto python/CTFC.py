from calculadoras.calculoCTFC import calcularCTFC

print("Calculadora de fahrenheit para celsius:")

fahrenheit = float(input("Digite a temperatura em fahrenhait e tecle ENTER, "\
"caso use números decimais utilize ponto ao invés de vírgula:"))
celsius = calcularCTFC(fahrenheit)

print(f"{fahrenheit}°F = {celsius:.2f}°C")