pessoas = list()
dado = list()
totpessoas = mai = men = 0 #Falta encontrar como fazer o maior e menor peso e o nome das pessoas
while True:
    dado.append(str(input("Nome: ")))
    dado.append(float(input("Peso [Kg]: ")))
    if len(pessoas) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    totpessoas += 1
    cont = str(input("Você quer continuar? [S/N] ")).strip().upper()[0]
    while cont not in "SsNn":
        cont = str(input("Você quer continuar? [S/N] ")).strip().upper()[0]
    if cont in "Nn":
        break
print("-="*30)
print(f"Ao todo você cadastrou {totpessoas} pessoas.")
print(f"O maior peso foi de {mai}kg, referente a", end=" ")
for p in pessoas:
    if p[1] == mai:
        print(f"{p[0]}.")
print(f"O menor peso foi de {men}kg, referente a", end=" ")
for p in pessoas:
    if p[1] == men:
        print(f"{p[0]}.")
print("-="*30)
