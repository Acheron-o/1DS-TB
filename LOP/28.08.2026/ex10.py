#Crie uma variável idade com o valor escolhido pelo usuário.
#Calcule quantos dias  de vida aproximadamente essa pessoa já viveu (considerando 365 dias por ano) e  imprima o resultado. 
ano = 365
idade = int(input("Digite a sua idade: "))
print(f"Sem considerar anos bissextos (quando o ano tem um dia a mais), você tem: {idade * 365} dias de idade")