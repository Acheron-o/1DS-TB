#Peça um númeor para o usuário e imprima se ele é par ou ímpar. E se é múltiplo de 3 ou de 5.

n = int(input("Digite um número: "))

if n%2 == 0:
    print(f"{n} é par.")
else:
    print(f"{n} é ímpar.")

if n%3 == 0:
    print(f"{n} é múltiplo de 3")
else:
    print(f"{n} não é múltiplo de 3")
if n%5 == 0:
    print(f"{n} é múltiplo de 5")
else:
    print(f"{n} não é múltiplo de 5")