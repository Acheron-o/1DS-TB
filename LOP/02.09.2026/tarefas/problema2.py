nota = float(input("Qual a sua nota? "))

if nota >= 95.0:
    print("Excelente!")
elif nota >= 70.0 and nota < 95.0:
    print("Boa!")
elif nota >= 50.0 and nota < 70.0:
    print("Média!")
else:
    print("Sua nota é insuficiente.")