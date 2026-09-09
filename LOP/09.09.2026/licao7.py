def triangle_type(c):
    if sum(c)/3 == c[0]:
        return "equilatero (todos os lados iguais)"
    elif c.count(c[0]) == 2 or c.count(c[1]) == 2:
        return "isóceles (apenas dois lados são iguais)"
    else:
        return "escaleno (todos os lados são diferentes)"
comprimentos = []
lados = 3
triangulo = False
for c in range(lados):
    comprimentos.append(int(input("Digite um comprimento de um lado de um triangulo: ")))
    comprimentos.sort()
if comprimentos[0] + comprimentos[1] > comprimentos[2]:
    print(f"Os números inseridos configuram um triângulo, este sendo {triangle_type(comprimentos)}.")
else:
    print(f"Os números inseridos são inválidos pois não configuram um triângulo completo.")
    
