from calculadoras.calculoCTCF import calcularCTCF

print("Calculadora de celsius para fahrenheit:")

celsius = float(input("Digite a temperatura em celsius e tecle ENTER, " \
"caso use números decimais utilize ponto ao invés de vírgula::"))
fahrenheit = calcularCTCF(celsius)

print(f"{celsius}°C = {fahrenheit:.2f}°F")