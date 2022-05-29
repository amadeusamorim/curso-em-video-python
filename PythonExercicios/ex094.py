pessoas = list()
dados = dict()
dados["nome"] = ""
dados["sexo"] = ""
dados["idade"] = 0
while True:
    dados["nome"] = input(str("Nome: ")).capitalize().strip()
    dados["sexo"] = input(str("Sexo [M/F]: ")).upper().strip()[0]
    while dados["sexo"] not in "MmFf":
        dados["sexo"] = input(str("Sexo [M/F]: ")).upper().strip()[0]
    dados["idade"] = input(int("Idade: "))
    continuar = input(str("Quer continuar? [S/N] ")).upper().strip()[0]
    while continuar not in "SsNn":
        continuar = input(str("Quer continuar? [S/N] ")).upper().strip()[0]
    if continuar == "N":
        break
print('-='*30)
print(dados)
