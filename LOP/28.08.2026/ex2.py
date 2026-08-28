def operacoes(a = 5, b = 10):
    operacoes = f"""
============================================
Os valores são a {a} e b {b}
============================================
A soma dos valores é igual a: {a+b}
A subtração dos valores é igual a: {a-b}
A multiplicação dos valores é igual a: {a*b}
A divisão dos valores é igual a: {a/b}
============================================"""
    return operacoes
#Os prinicipais valores são a e b, eles são respectivamente 5 e 10 , entretanto é possível altera-los, as declarando no momento em que a função é encontrada
print(operacoes(a = 25, b = 90)) # Um exemplo das variaveis sendo mudadas dentro aos parâmetros da função