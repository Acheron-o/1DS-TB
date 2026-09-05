#Calcule a distância entre dois pontos em 3D.
import math
x1 = float(input("Digite a coordenada x1: "))
x2 = float(input("Digite a coordenada x2: "))
y1 = float(input("Digite a coordenada y1: "))
y2 = float(input("Digite a coordenada y2: "))
z1 = float(input("Digite a coordenada z1: "))
z2 = float(input("Digite a coordenada z2: "))

d = math.sqrt(math.pow((x2 - x1),2) + math.pow((y2 - y1),2) + math.pow((z2 - z1,2)))

print(f"A distância entre dois pontos nas coordenadas oferecidas: ")
