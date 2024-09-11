# Crie um programa que receba a idade de uma pessoa e classifique-a de acordo com as seguintes faixas etárias:
# Criança (0-12 anos)
# Adolescente (13-17 anos)
# Adulto (18-59 anos)
# Idoso (60 anos ou mais)

idade = int(input("digite a idade"))

if idade <= 12:
    print ("voce é uma criança")
elif idade <= 17:
    print ("voce é um adolescente")
elif idade <=59:
    print ("voce é um aulto")
if idade >= 60:
    print ("voce é um idoso")
    