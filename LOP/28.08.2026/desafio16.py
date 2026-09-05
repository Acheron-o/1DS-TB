#Crie quatro variáveis, x1, y1, x2 e y2, 
# representando as coordenadas de dois  pontos no plano cartesiano (por exemplo, x1 = 1, y1 = 2, x2 = 4, y2 = 6). 
# Os  valores devem ser solicitados pelo usuário. 
# Calcule a distância entre esses dois  pontos usando a fórmula da distância euclidiana

import math

x1 = int(input("Digite o valor x da primeira coordenada: "))
y1 = int(input("Digite o valor y da primeira coordenada: "))
x2 = int(input("Digite o valor x da segunda coordenada: "))
y2 = int(input("Digite o valor y da segunda coordenada: "))

primeira_coordenada = (x1,y1)
segunda_coordenada = (x2,y2)

distancia = math.sqrt((primeira_coordenada[1] - primeira_coordenada[0])**2 + (segunda_coordenada[1] - segunda_coordenada[0])**2 )

print(f"O valor da distância entre os dois pontos mostrados 1° {primeira_coordenada}, e 2° {segunda_coordenada} é: {distancia}")
