def preco_final(preco = 50, desconto = 10):
    return preco - (preco * (desconto/100))

#Os parâmetros da função, tem como serem editados e assim suprindo qualquer diferente situação, porem como padrão, os valores estão conforme o problema no documento.
print(f"O preço final foi: {preco_final()}R$")