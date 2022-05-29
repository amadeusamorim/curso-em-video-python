lista = list()
r = ""
while True:
    n = int(input("Digite um valor: "))
    if n not in lista:
        lista.append(n)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado! Não vou adicionar...")
    r = (str(input("Você quer continuar? [S/N] "))).strip().upper()[0]
    while r not in "SN":
        r = (str(input("Você quer continuar? [S/N] "))).strip().upper()[0]
    if r == "N":
        break
print("-="*25)
print(f"Sua lista registrada em ordem é: {sorted(lista)}.")
