from calculadoras.calculoCTCF import calcularCTCF

print("Calculadora de celsius para fahrenheit:")

celsius = float(input("Digite a temperatura em celsius:"))
fahrenheit = calcularCTCF(celsius)

print(f"{celsius}°C = {fahrenheit: .2f}°F")