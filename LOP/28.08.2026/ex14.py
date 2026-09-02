#Crie duas variáveis, a e b, com valores escolhidos pelo usuário. 
# Troque os valores  dessas variáveis sem usar uma terceira variável e imprima os novos valores de a e b.

a = int(input("Digite um primeiro número: "))
b = int(input("Digite um segundo número: "))
print(f"O primeiro número é {a} e o segundo número é {b}.")
a,b = b,a
print(f"O primeiro número agora é {a} e o segundo agora é {b}.")
