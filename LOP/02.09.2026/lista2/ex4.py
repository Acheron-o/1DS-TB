#Declare duas variáveis a e b, e peça valores inteiros a elas. Realize a troca de conteúdo entre a e b. Exiba os valores antes da troca e depois da troca.

a = int(input("Diga o valor inteiro da variável a: "))
b = int(input("Diga o valor inteiro da variável b: "))
print(f"a e b são respectivamente: {a}, {b}")
a,b = b,a
print(f"a e b agora são respectivamente: {a}, {b}")
