def elegivel(idade, renda_mensal):
    perfil = (idade,renda_mensal)

    pode_fazer = False
    if perfil[0] >= 18 and perfil[1] > 1500:
        pode_fazer = True
        return pode_fazer
    elif perfil[0] < 18 and perfil[1] > 1000:
        pode_fazer = True
        return pode_fazer
    return pode_fazer

idade = float(input("Digite a sua idade: "))
renda_mensal = float(input("Digite a sua renda mensal: "))

if elegivel(idade,renda_mensal):
    print("Meus parabéns, você tem elegibilidade para realizar um empréstimo!!!")
else:
    print("Infelizmente, com base nos dados fornecidos você não é elegível para realizar empréstimos!!!")


    
    