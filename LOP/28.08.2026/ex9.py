#Crie duas variáveis, num1 e num2, com valores solicitados ao usuário,  respectivamente. Verifique se num1 é maior que num2 e imprima o resultado  (True ou False). SEM USAR IF-ELIF-ELSE. x = int(input("Digite o primeiro número: "))
def true_ou_false(num1 = 0, num2 = 0):
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    return print(f"Sobre o primeiro número ser maior que o segundo número: {num1 > num2}")
true_ou_false()
