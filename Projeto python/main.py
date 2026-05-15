from analises.analisesIMC import calcularIMC
from calculadoras.calculoIMC import analisarIMC

print("Calculadora de IMC:")
nomePessoa = str(input("Escreva o seu nome e tecle ENTER:"))
alturaPessoa = float(input("Escreva a sua altura, utilizando ponto ao invès de vírgula e tecle ENTER:"))
pesoPessoa = float(input("Escreva o seu peso, utilizando ponto ao invès de vírgula e tecle ENTER:"))

imc = calcularIMC(pesoPessoa, alturaPessoa)

analisarIMC(imc, nomePessoa)