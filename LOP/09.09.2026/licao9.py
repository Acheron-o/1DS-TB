#Jogo de Pedra, Papel e Tesoura.
#Crie um jogo de Pedra, Papel e Tesoura em que o usuário jogue contra o computador

import random 

maos = ["papel","tesoura","pedra"] #Valores respectivos de 0,1,2 para as mãos

pc = random.choice(maos)

player = input("Escolhe entre pedra, papel e tesoura: ").lower()
print(f"Sua escolha foi {player}")
print(f"A escolha do computador foi {pc}")
vencedor = (maos.index(player) - maos.index(pc) + 3) % 3


if vencedor == 1:
    print("Você venceu parabéns")
elif vencedor == 2:
    print("O computador venceu que pena")
else:
    print("Deu empate")
