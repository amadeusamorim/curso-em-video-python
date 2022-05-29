#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salário = float(input("Qual o seu salário? "))
aumento = salário * 0.15

if salário > 1250:
    aumento = salário * 0.10

print("Boas notícias, seu aumento será de R${:.2f}, agora você receberá {:.2f}".format(aumento, (aumento+salário)))