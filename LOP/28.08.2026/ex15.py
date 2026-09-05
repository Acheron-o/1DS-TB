# Crie três variáveis, nota1, nota2 e nota3, com valores escolhidos pelo usuário.
# Calcule a média ponderada dessas notas, onde os pesos são 2, 3 e 5,  respectivamente. Imprima o resultado. 

nota1 = float(input("Digite o número da primeira nota: "))
nota2 = float(input("Digite o número da segunda nota: "))
nota3 = float(input("Digite o número da terceira nota: "))

notas = [nota1,nota2,nota3]
medias_respectivas = (2,3,5)
idx = 0
resultado = 0
for i in medias_respectivas:
    resultado += notas[idx]/i
    idx += 1
print(f"O resultado final (médias das notas dados os pesos) é: {resultado:.2f}")