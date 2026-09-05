import math
#Leia três números e calcule média aritmética, geométrica e harmônica.
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

numeros = [n1,n2,n3]

media_aritimetica = sum(numeros)/len(numeros)
media_geometrica = math.sqrt(sum(numeros))
media_harmonica = len(numeros)/(1/numeros[0] + 1/numeros[1] + 1/numeros[2])

print(f"A média aritimética dos valores apresentados é: {media_aritimetica}")
print(f"A média aritimética dos valores apresentados é: {media_geometrica}")
print(f"A média aritimética dos valores apresentados é: {media_harmonica}")


