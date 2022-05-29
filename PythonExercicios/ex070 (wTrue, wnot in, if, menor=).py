print('---'*10)
print("{:^30}".format("BARATO DEMAIS"))
print('---'*10)
total = caro = cont = prodmil = barato = 0
sair = nomebarato = ""
while True:
    nome = str(input("Nome do produto: ")).strip().lower()
    preço = float(input("Preço: R$"))
    total += preço
    cont += 1
    sair = str(input("Quer continuar?: [S/N] ")).strip().lower()[0]
    while sair not in "SsNn":
        sair = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if preço > 1000:
        prodmil += 1
    if cont == 1:
        barato = preço
        nomebarato = nome
    else:
        if preço < barato:
            barato = preço
            nomebarato = nome
    if sair == "n":
        break
print("{:-^40}".format("FIM DO PROGRAMA"))
print(f"O total da compra foi de R${total:.2f}.")
print(f"Temos {prodmil} produtos custando mais de R$1.000,00.")
print(f"O produto mais barato foi {nomebarato} que custa R${barato:.2f}.")
