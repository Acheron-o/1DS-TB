#Calcule o cosseno da lei dos cossenos para encontrar um lado.

import math

lado_a = 5
lado_b = 7
angulo_C = 60

angulo_C_radiano = math.radians(angulo_C)

c_ao_quadrado = lado_a**2 + lado_b**2 - (2 * lado_a * lado_b * math.cos(angulo_C_radiano))

lado_c = math.sqrt(c_ao_quadrado)

print(f"A largura do lado faltante (c) é: {lado_c:.2f}")