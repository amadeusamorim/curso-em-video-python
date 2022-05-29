print("{:*^40}".format("AMA PLACE"))
preco = float(input("Preço das compras: R$"))
print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão, digite
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")

pag = int(input("Qual a opção desejada? "))

if pag == 1:
    print("Sua compra de R${} vai custar R${:.2f} no final.".format(preco, preco*0.90))
elif pag == 2:
    print("Sua compra de R${} vai custar R${:.2f} no final.".format(preco, preco*0.95))
elif pag == 3:
    print("Sua compra será parcelada em 2x de {:.2f}, sem juros. Seu valor final será {:.2f}.".format(preco/2, preco))
elif pag == 4:
    parcelas = int(input("Quantas parcelas? "))
    print("Sua compra será parcelada em R${}x de R${:.2f} COM JUROS.".format(parcelas, (preco*1.20)/parcelas))
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(preco, preco*1.20))
else:
    print("Opção inválida!")