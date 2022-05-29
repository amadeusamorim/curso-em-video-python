geral = list()
par = list()
impar = list()
continuar = ""
while True:
    geral.append(int(input("Digite um número: ")))
    continuar = str(input("Você deseja continuar? [S/N] ")).strip().upper()[0]
    while continuar not in "SN":
        continuar = str(input("Você deseja continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
for i, v in enumerate(geral):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print("-="*30)
print(f"Sua lista completa é {geral}.")
print(f"Sua lista de pares é {par}.")
print(f"Sua lista de ímpares é {impar}.")
