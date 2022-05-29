from datetime import date
from datetime import datetime
func = dict()
func["Nome"] = str(input("Nome do funcionário: ")).capitalize().strip()
nasc = int(input("Ano de nascimento: "))
func["Idade"] = date.today().year - nasc
func["CTPS"] = int(input("Carteira de trabalho (0 não tem): "))
if func["CTPS"] != 0:
    func["Contratação"] = int(input("Ano de Contratação: "))
    func["Salário"] = float(input("Salário: R$"))
    func["Aposentadoria"] = func["Idade"] + (func["Contratação"] + 35) - datetime.now().year
print("-="*30)
for k, v in func.items():
    print(f"  - {k} tem o valor {v}.")
