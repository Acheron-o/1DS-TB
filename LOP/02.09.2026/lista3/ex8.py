#Calcule o volume de um tronco de cone.
import math

PI = 3.1415
h = float(input("Qual a altura do tronco: "))
R = float(input("Qual o raio da base maior: "))
r = float(input("Qual o raio da base menor: "))

V = 1/3 * PI * h * (R**2 + R * r + r**2)

print(f"O volume do tronco de um cone, com as informações fornecidas é: {V:.2f}")