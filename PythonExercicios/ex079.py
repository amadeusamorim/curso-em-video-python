lista = list()
cont = ""
while True:
    lista.append(int(input("Digite um valor: ")))
    print("Valor adicionado com sucesso...")
    cont = (str(input("Você quer continuar? [S/N] "))).strip().upper()
    while cont not in "SN":
        cont = (str(input("Você quer continuar? [S/N] "))).strip().upper()[0]
    if cont == "N":
        break
print("-="*25)
print(f"Sua lista registrada em ordem é: {sorted(lista)}.")
