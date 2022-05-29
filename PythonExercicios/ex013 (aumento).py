#Reajuste salarial

wage=float(input("Qual é o salário do funcionário? R$"))
aumento=float(wage*1.15)

print("O funcionário que recebia R${:.2f}, teve 15% de aumento e agora seu salário é R${:.2f}".format(wage, aumento))