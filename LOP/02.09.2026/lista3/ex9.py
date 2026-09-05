#Aplique a fórmula de Heron para área de um triângulo.
import math

a = float(input("Digite o lado a do triângulo: "))
b = float(input("Digite o lado b do triângulo: "))
c = float(input("Digite o lado c do triângulo: "))

s = a + b + c / 2

A = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f"A área do triângulo com os três lados oferecidos é: {A:.2f}")
