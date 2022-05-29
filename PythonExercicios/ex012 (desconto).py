#Calculando descontos

preço=float(input("Qual o preço do produto? R$"))
novo= preço-(preço*5/100)

print("O preço do produto é {:.2f}, mas no cartão da loja, conseguimos um desconto especial de 5% e a peça sairá a R${:.2f}.".format(preço, novo))