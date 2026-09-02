#Peça um número para o usuário e imprima a classificação de idade:

idade = int(input("Digite uma idade para classificarmos: "))
if idade < 0:
    print("Espermatozoide")
elif idade < 2:
    print("Bebê")
elif idade < 13:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 67:
    print("Adulto")
else:
    print("Idoso")

