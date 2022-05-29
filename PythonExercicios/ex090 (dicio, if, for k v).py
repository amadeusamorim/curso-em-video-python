aluno = dict()
aluno["Nome"] = str(input("Nome: ")).strip().capitalize()
aluno["Média"] = float(input(f"Média do {aluno['Nome']}: "))
aluno["Situação"] = ""
if aluno["Média"] >= 7:
    aluno["Situação"] = "aprovado"
elif 5 <= aluno["Média"] < 7:
    aluno["Situação"] = "em recuperação"
else:
    aluno["Situação"] = "reprovado"
print("-="*30)
for k, v in aluno.items():
    print(f"  * {k} é igual a {v}.")