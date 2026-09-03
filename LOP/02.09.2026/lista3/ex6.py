#Verifique se um número pertence ao intervalo [10,100] usando apenas operadores relacionais e lógicos.
n = int(input("Digite um número: "))
pertence = n in range(10,100 + 1)
print(f"O número {n}, pertence ao intervalo [10,100]? {pertence}")