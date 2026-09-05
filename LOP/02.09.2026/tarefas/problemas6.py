#Conversor de unidades. Escreva um programa que permite ao usuário escolher entre converteer uma temperatura de celsius para fahrenheit ou vice-versa. Socilite o valor e execute a conversão:

while True:
    print("""
===============================================================================================================================
Por gentileza escolha uma dentre as duas conversões abaixo para serem realizadas (digitando os seus correspondente números):

1 - Celsius para Fahrenheit
2 - Fahrenheit para Celsius
===============================================================================================================================""")
    escolha = int(input("Digite aqui: "))
    if escolha == 1:
        temperatura = float(input("Escolha o valor da temperatura: "))
        print(f"{temperatura} celsius em fahrenheit é {(temperatura * 1.8) + 32}")
        break
    elif escolha == 2:
        temperatura = float(input("Escolha o valor da temperatura: "))
        print(f"{temperatura} fahrenheit em celsius é {(temperatura - 32)/1.8} ")
        break
    else:
        print("Escolha inválida tente novamente")
        continue