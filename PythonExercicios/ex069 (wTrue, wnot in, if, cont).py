idade = mais18 = h = mu20 = 0
while True:
    print("--" * 20)
    print("    CADASTRE UMA PESSOA")
    print("--" * 20)
    idade = int(input("Idade: "))
    sexo = continuar = ""
    sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    while sexo not in "MmFf":
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    if idade > 18:
        mais18 += 1
    if sexo == "M":
        h += 1
    if sexo == "F" and idade < 20:
        mu20 += 1
    while continuar not in "SsNn":
        continuar = str(input("Você quer continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
            break
print("======== FIM DO PROGRAMA ========")
print(f"O total de pessoas com mais de 18 anos foi: {mais18}")
print(f"Ao todo temos {h} homens cadastrados.")
print(f"E temos {mu20} mulheres com menos de 20 anos.")
