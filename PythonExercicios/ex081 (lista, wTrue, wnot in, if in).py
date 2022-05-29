lista = []
cont = ""
c = 0
while True:
    lista.append(int(input("Digite um valor: ")))
    cont = str(input("Você deseja continuar? [S/N] ")).strip().upper()[0]
    while cont not in "SN":
        cont = str(input("Você deseja continuar? [S/N] ")).strip().upper()[0]
    if cont == "N":
        break
print(f"A sua lista teve {len(lista)} elementos digitados.")
print(f"Sua lista final é {sorted(lista, reverse=True)}.")
if 5 in lista:
    print("O valor 5 foi digitado na lista.")
else:
    print("O valor 5 não foi encontrado na lista.")
