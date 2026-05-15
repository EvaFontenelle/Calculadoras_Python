def analisarIMC(imc, nomePessoa):
    
    if imc <= 18.5:
        print(imc)
        print(nomePessoa, "o seu IMC está em baixo peso do normal!")
    elif imc > 18.6 and imc <= 24.9:
        print(imc)
        print(nomePessoa, "o seu IMC está em peso normal!")
    elif imc >= 25.0 and imc <= 29.9:
        print(imc)
        print(nomePessoa, "o seu IMC está considerado sobrepeso!")
    elif imc >= 30.0 and imc <= 34.9:
        print(imc)
        print(nomePessoa, "o seu IMC é considerado obesidade grau I.")
    elif imc >= 35.0 and imc <= 39.9:
        print(imc)
        print(nomePessoa, "o seu IMC é considerado obesidade grau II.")
    elif imc >= 40.0:
        print(imc)
        print(nomePessoa, "o seu IMC é considerado obesidade grau III...")
    else:
        print("Informe os dados corretamente!")