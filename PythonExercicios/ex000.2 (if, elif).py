name = str(input("Qual o nome do funcionário? "))
wage = float(input("Qual o salário do funcionário? R$"))
dep = int(input("Qua a quantidade de dependentes? "))

if dep == 0:
    nwage = wage * 1.05
elif dep <=3:
    nwage = wage * 1.10
elif dep <=6:
    nwage = wage * 1.15
else:
    nwage=wage * 1.18

print("O novo salário de {} será de {:.2f}.".format(name, nwage))