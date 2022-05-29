galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa["nome"] = input(str("Nome: ")).capitalize().strip()
    while True:
        pessoa["sexo"] = input(str("Sexo [M/F]: ")).upper().strip()[0]
        if pessoa["sexo"] in "MF":
            break
        print("ERRO! Por favor, digite apenas M ou F.")
    pessoa["idade"] = int(input("Idade: "))
    soma += pessoa["idade"]
    galera.append(pessoa.copy())
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
        if resp in "SN":
            break
        print("ERRO! Por favor, responda apenas com S ou N.")
    if resp == "N":
        break
print("-="*30)
print(f"A)  Ao todo temos {len(galera)} pessoas cadastradas.")
média = soma / len(galera)
print(f"B)  A média de idade é de {média:5.2f} anos.")
print("C)  As mulheres cadastradas foram ", end="")
for p in galera:
    if p["sexo"] == "F":
        print(f"{p['nome']} ", end="")
print()
print("D)  Lista das pessoas que estão acima da média de idade: ")
for p in galera:
    if p["idade"] >= média:
        print("    ", end="")
        for k, v in p.items():
            print(f"{k} = {v}; ", end="")
        print()
print("<<< ENCERRADO >>>")
