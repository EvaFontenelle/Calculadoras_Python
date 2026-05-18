from analises.analisesIMC import analisarIMC
from calculadoras.calculoIMC import calcularIMC

print("Calculadora de IMC:")
nomePessoa = str(input("Escreva o seu nome e tecle ENTER:"))
alturaPessoa = float(input("Escreva a sua altura, utilizando ponto ao invés de vírgula e tecle ENTER:"))
pesoPessoa = float(input("Escreva o seu peso, utilizando ponto ao invés de vírgula e tecle ENTER:"))

imc = calcularIMC(pesoPessoa, alturaPessoa)

analisarIMC(imc, nomePessoa)