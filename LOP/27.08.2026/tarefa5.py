#Socilitar ao usuário o valor das seguintes receitas e despesas:
"""
As variaveis a baixo n_de_receitas , n_de_despesas; são dinâmicas, 
isso é dependendo da quantidade de despesas e receitas, ele consegue calcular normalmente, 
basta alteralas livremente
"""
n_de_receitas = 3
n_de_despesas = 3
#variaveis que não é recomendado mudar
receitas = []
despesas = []
print("Bem-vindo ao sistema de gerenciamento de finanças pessoais!")
print("Você irá cadastrar receitas e despesas, calcular o saldo e gerar um\nrelatório detalhado.")
for receita in range(1, n_de_receitas + 1):
    receitas.append(float(input(f"Digite a receita numero {receita}: ")))
for despesa in range(1,n_de_despesas + 1):
    despesas.append(float(input(f"Digite a despesa numero {despesa}: ")))
#calcular o numero total de receitas e despesas
total_receita = sum(receitas)
total_despesa = sum(despesas)
#Calcular o saldo por calcular a diferença da receita pelas despesas
saldo = total_receita - total_despesa
#Agrupar os percentuais de despesas     
percentuais_despesas = []
percentuais_receitas = []
for despesa in despesas:
    percentuais_despesas.append((despesa/total_despesa) * 100)
for receita in receitas:
    percentuais_receitas.append((receita/total_receita)*100)
#Gerar um relatório detalhado com as seguintes informações
print("==========================================================")
print("               RELATORIO DAS RECEITAS E DESPESAS")
print("==========================================================")
print(f"O total de receitas calculadas é: {total_receita}")
print(f"O total de despesas calculadas é: {total_receita}")
print(f"O saldo final é: {saldo}")
#Um contador, apenas para deixar os prints mais organizados
contador_percent_despesas = 1
contador_percent_receitas = 1
for percentual in percentuais_despesas:
    print(f"O percentual da despesa numero {contador_percent_despesas}: {percentual}%")
    contador_percent_despesas += 1
for percentual in percentuais_receitas:
    print(f"O percentual da receita numero {contador_percent_receitas}: {percentual}%")
    contador_percent_receitas += 1
