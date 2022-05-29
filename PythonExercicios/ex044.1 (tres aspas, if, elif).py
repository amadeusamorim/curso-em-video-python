print("{:*^40}".format("AMA PLACE"))
preco = float(input("Preço das compras: R$"))
print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão, digite
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
opcao = int(input("Qual a opção desejada? "))
if opcao == 1:
    total = preco * 0.90
elif opcao == 2:
    total = preco * 0.95
elif opcao == 3:
    total = preco
    parcela = total/2
    print("Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.".format(parcela))
elif opcao == 4:
    total = preco * 1.20
    totparc = int(input("Quantas parcelas? "))
    parcela = total/totparc
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS.".format(totparc, parcela))
else:
    print("Opção inválida de pagamento. Tente novamente.")

print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preco, total))
