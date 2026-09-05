#Declare duas variáveis saldo e divida. Solicite que o usuário insira os valores e exiba-os na tela.

saldo = float(input("Digite o seu saldo em R$: "))
divida = float(input("Digite a sua divida em R$: "))

output = f"""================================================
                            Saldo e Dividas
            ==================================================
Seu saldo é: {saldo}R$
Sua dívida é: {divida}R$

O valor restante após a divida ser paga será de: {divida - saldo}R$
============================================================================"""


