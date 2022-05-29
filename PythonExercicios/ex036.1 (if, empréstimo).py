#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print("-"*25)
print("CAIXA ECONÔMICA FEDERAL")
print("-"*25)

valor = float(input("Qual o valor do imóvel desejado? R$"))
wage = float(input("Qual o salário do comprador? R$"))
tempo = int(input("Em quantos anos você deseja quitar o imóvel? "))

prestacao = valor/(tempo*12)
comppct = (prestacao/wage)*100

print("Para pagar um imóvel de R${:.2f}, a prestação será de R${:.2f} em {} anos.".format(valor, prestacao, tempo))

if prestacao > wage * 0.30:
    print("Empréstimo NEGADO.")
else:
    print("Empréstimo pode ser CONCEDIDO.")
