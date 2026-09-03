#Calcule a área de um hexágo no regular dado o lado.
import math


lado = float(input("Qual o lado do hexágono para calcular sua área: "))
area = 3*math.sqrt(3)/2 * math.pow(lado,2)
print(f"A área do hexágono com lado {lado:.0f} é: {area:.2f}")