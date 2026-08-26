nome1 = "aula"
nome2 = "Python"
copia2 = nome2
print(f"Este é a variavel nome 1: {nome1}")
print(f"Este é a variavel nome 2: {nome2}")
nome2 = nome1
nome1 = copia2
print(f"Este é a variavel nome 1, agora após a inversão de valores: {nome1}")
print(f"Este é a variavel nome 2, agora após a inversão de valores: {nome2}")
#atribuição multiplas de valores
nome1_teste, nome2_teste = nome2, nome1 #isso faz uma atribuição multipla e linear, ignorando os problemas relacionados a ponteiros na memória      
